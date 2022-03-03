import os
import glob

from pathlib import Path

import pandas as pd

tsv_PATH = './tsv_from_AIS'

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

def merge_tsv_files(PATH):
    # read tsv files
    tsv_files = glob.glob(PATH+'/*.tsv')
    # array of data frames
    frames = []
    for file in tsv_files:
        # read lines in file
        lines = open(file, encoding="cp932").readlines()
        # remove the first 3 lines
        open(file, 'w').writelines(lines[3:])
        # convert file to dataframe
        df = pd.read_csv(file, sep='\t', header=None)
        # append data frame to array
        frames.append(df)

    # concantenate data frames
    result = pd.concat(frames)
    # add columns to data frame
    result.columns = columns
    # output data frame as tsv file
    result.to_csv('./output.tsv', sep='\t', index=False)
    # output data frame as excel file
    # result.to_excel('./output.xlsx', index=False)


merge_tsv_files(tsv_PATH)

