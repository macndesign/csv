# coding: utf-8
import csv
from collections import namedtuple

with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for r in f_csv:
        print('Symbol: {0}, Price: {1}'.format(r['Symbol'], r['Price']))
