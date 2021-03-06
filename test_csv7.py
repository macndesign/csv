# coding: utf-8
import csv, re

col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)
