from aptos_sdk.account import Account
from utils.Sui_utils import PublicKeyUtils
from hashlib import blake2b
from aptos_sdk.bcs import Serializer
from aptos_sdk.ed25519 import PublicKey


def generate_sui_address(public_key: PublicKey, signature_flag: int) -> str:
    serializer = Serializer()
    serializer.u8(signature_flag)
    serializer.fixed_bytes(public_key.key.encode())
    serialized_data = serializer.output()

    hashed = blake2b(serialized_data, digest_size=32)
    address = hashed.digest()
    return "0x" + address.hex()


def get_sui_wallet_info(seed_phrases):
    wallet_info = []
    signature_flag = 0x00  # Флаг схемы подписи для Ed25519

    for seed_phrase in seed_phrases:
        pt_seed = PublicKeyUtils(seed_phrase)
        keys = Account.load_key(pt_seed.private_key.hex())
        public_key = keys.public_key()
        address = generate_sui_address(public_key, signature_flag)
        private_key = keys.private_key.hex()

        wallet_info.append({
            'Seed Phrase': seed_phrase,
            'Address': address,
            'Public Key': public_key,
            'Private Key': private_key
        })

    return wallet_info
