from generate_wallet import generate_wallets
from aptos_data import get_aptos_wallet_info
from sui_data import get_sui_wallet_info
import openpyxl

num_wallets = int(input("Введите количество кошельков для генерации: "))

wallet_phrases = generate_wallets(num_wallets)

aptos_wallet_info = get_aptos_wallet_info(wallet_phrases)
sui_wallet_info = get_sui_wallet_info(wallet_phrases)

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet.cell(row=1, column=1, value="Seed Phrase")
sheet.cell(row=1, column=2, value="Aptos Address")
sheet.cell(row=1, column=3, value="Public Key")
sheet.cell(row=1, column=4, value="Private Key")
sheet.cell(row=1, column=5, value='Sui Address')
sheet.cell(row=1, column=6, value="Public Key")
sheet.cell(row=1, column=7, value="Private Key")

for i, info in enumerate(aptos_wallet_info, start=2):
    sheet.cell(row=i, column=1, value=info['Seed Phrase'])
    sheet.cell(row=i, column=2, value=str(info['Address']))
    sheet.cell(row=i, column=3, value=str(info['Public Key']))
    sheet.cell(row=i, column=4, value=str(info['Private Key']))

for i, info in enumerate(sui_wallet_info, start=2):
    sheet.cell(row=i, column=5, value=str(info['Address']))
    sheet.cell(row=i, column=6, value=str(info['Public Key']))
    sheet.cell(row=i, column=7, value=str(info['Private Key']))

workbook.save('MartianWallets.xlsx')

print("Результаты сохранены в файле MartianWallets.xlsx.")