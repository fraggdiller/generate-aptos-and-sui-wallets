from hashlib import blake2b
from aptos_sdk.account import Account
from utils.Aptos_utils import PublicKeyUtils
from utils.Sui_utils import SuiPublicKeyUtils
from aptos_sdk.bcs import Serializer
from aptos_sdk.ed25519 import PublicKey


class Wallet:
    def __init__(self, seed_phrase):
        self.seed_phrase = seed_phrase
        self.aptos_address = None
        self.aptos_private_key = None
        self.sui_address = None
        self.sui_private_key = None

    def generate_aptos_keys(self):
        pt_seed = PublicKeyUtils(self.seed_phrase)
        keys = Account.load_key(pt_seed.private_key.hex())
        self.aptos_address = keys.address()
        self.aptos_private_key = keys.private_key.hex()

    def generate_sui_keys(self):
        pt_seed = SuiPublicKeyUtils(self.seed_phrase)
        keys = Account.load_key(pt_seed.private_key.hex())
        public_key = keys.public_key()
        self.sui_address = self.generate_sui_address(public_key)
        self.sui_private_key = keys.private_key.hex()

    @staticmethod
    def generate_sui_address(public_key: PublicKey) -> str:
        serializer = Serializer()
        serializer.u8(0x00)
        serializer.fixed_bytes(public_key.key.encode())
        serialized_data = serializer.output()

        hashed = blake2b(serialized_data, digest_size=32)
        address = hashed.digest()
        return "0x" + address.hex()
