import os
import glob
import shutil

from pathlib import Path

import pandas as pd

csv_src_dir = './csv_from_AIS'

csv_upload_dir = './csv_upload'

csv_files = glob.glob('./csv_from_AIS/*.tsv')

frames = []
for file in csv_files:
    lines = open(file, encoding="cp932").readlines()
    open(file, 'w').writelines(lines[3:])
    df = pd.read_csv(file, sep='\t', header=None)
    frames.append(df)

result = pd.concat(frames)

columns = ['sku',
           'product-id',
           'product-id-type',
           'optional-payment-type-exclusion',
           'merchant_shipping_group_name',
           'price',
           'standard-price-points-percent',
           'minimum-seller-allowed-price',
           'maximum-seller-allowed-price',
           'item-condition',
           'quantity',
           'add-delete',
           'will-ship-internationally',
           'item-note',
           'handling-time']

result.columns = columns

print(result)

result.to_csv('./output.tsv', sep='\t', index=False)
# result.to_excel('./output.xlsx', index=False)

