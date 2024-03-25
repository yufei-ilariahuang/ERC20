from brownie import accounts, config, TokenERC20

initial_supply = 100
token_name = "TOKEN"
token_symbol = "TKN"
def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}
    )