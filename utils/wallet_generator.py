from mnemonic import Mnemonic
from utils.wallet_saver import WalletSaver
from utils.wallet import Wallet


class WalletGenerator:
    def __init__(self, num_wallets):
        self.num_wallets = num_wallets
        self.wallets = []

    def generate_wallets(self):
        for _ in range(self.num_wallets):
            seed_phrase = Mnemonic('english').generate()
            wallet = Wallet(seed_phrase)
            wallet.generate_aptos_keys()
            wallet.generate_sui_keys()
            self.wallets.append(wallet)

        WalletSaver.save_wallets_to_files(self.wallets)
