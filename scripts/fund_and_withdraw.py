from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpers import *


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFeeInWei()
    print(f"The current entry fee is {float(entrance_fee)}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee, "gas_price": gas_strategy})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
