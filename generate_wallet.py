from mnemonic import Mnemonic


def generate_wallets(num_wallets):
    wallet_phrases = []

    for _ in range(num_wallets):
        seed_phrase = Mnemonic('english').generate()
        wallet_phrases.append(seed_phrase)

    return wallet_phrases
