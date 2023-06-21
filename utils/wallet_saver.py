import csv
import os


class FileSaver:
    @staticmethod
    def save_to_csv(data, file_name):
        file_path = os.path.join('data', file_name)
        with open(file_path, 'w', newline='') as csv_file:
            csv.writer(csv_file).writerows(data)

    @staticmethod
    def save_to_text(data, file_name):
        file_path = os.path.join('data', file_name)
        with open(file_path, 'w') as txt_file:
            txt_file.write('\n'.join(str(item) for item in data))


class WalletSaver:
    @staticmethod
    def save_wallets_to_files(wallets):
        file_saver = FileSaver()

        attributes = ['seed_phrase', 'aptos_address', 'aptos_private_key', 'sui_address', 'sui_private_key']
        filenames = ['seeds.txt', 'aptos_addresses.txt', 'aptos_private_keys.txt', 'sui_addresses.txt', 'sui_private_keys.txt']

        for attr, filename in zip(attributes, filenames):
            file_saver.save_to_text([getattr(wallet, attr) for wallet in wallets], filename)

        csv_data = [
            ["Seed Phrase", "Aptos Address", "Aptos Private Key", "Sui Address", "Sui Private Key"]
        ] + [[getattr(wallet, attr) for attr in attributes] for wallet in wallets]

        file_saver.save_to_csv(csv_data, 'wallets.csv')
