# coding: utf-8
import csv, re

field_types = [('Price', float), ('Change', float), ('Volume', int)]
with open('stocks.csv') as f:
     for row in csv.DictReader(f):
         row.update((key, conversion(row[key]))
                    for key, conversion in field_types)
         print(row)
