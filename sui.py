from pysdk_sui import Wallet

faucet_url_ = 'https://faucet.devnet.sui.io/gas'
rpc_url_ = 'https://fullnode.devnet.sui.io/'
mnemonic = 'spell front unit nephew true glow ecology release dutch giggle lawn catch'

wallet = Wallet(rpc_url=rpc_url_, faucet_url=faucet_url_, mnemonic=mnemonic)


def example_wallet():
    my_wallet_info = wallet.get_wallet_info()
    print(f"Mnemonic: {my_wallet_info.mnemonic}")
    print(f"Private Key: {my_wallet_info.private_key.hex()}")  # Convert bytes to hexadecimal string
    print(f"Public Key: {my_wallet_info.public_key.hex()}")  # Convert bytes to hexadecimal string
    print(f"Address: {my_wallet_info.address}")


example_wallet()
