from aptos_sdk.account import Account
from utils.Aptos_utils import PublicKeyUtils


def get_aptos_wallet_info(seed_phrases):
    wallet_info = []

    for seed_phrase in seed_phrases:
        pt_seed = PublicKeyUtils(seed_phrase)
        keys = Account.load_key(pt_seed.private_key.hex())
        address = keys.address()
        public_key = keys.public_key()
        private_key = keys.private_key.hex()

        wallet_info.append({
            'Seed Phrase': seed_phrase,
            'Address': address,
            'Public Key': public_key,
            'Private Key': private_key
        })

    return wallet_info
