from brownie import accounts, config, network, MockV3Aggregator
from brownie.network.gas.strategies import LinearScalingStrategy
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 2e11

MAINNET_FORK = ["mainnet-fork-infura", "mainnet-fork-alch"]
LOCAL_BLOCKCHAIN = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN + MAINNET_FORK:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f"Deploying mocks...")
    if len(MockV3Aggregator) == 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            STARTING_PRICE,
            {"from": get_account(), "gas_price": gas_strategy},
        )
    print(f"Mocks deployeds!")


gas_strategy = LinearScalingStrategy("100000000 wei", "5 gwei")
