import pandas as pd
import sqlite3

import os


con = sqlite3.connect('CambridgeDictionary.db')
cur = con.cursor()


filename = 'data/dictionary.csv'
df = pd.read_csv(filename)
print(f"读取{filename}成功")
data = df.values
data = list(map(lambda x: tuple(x), data))
cur.executemany(
    'insert into dictionary (word, wordType, phoneticSymbol, definition, examples) values (?, ?, ?, ?, ?)',
    data)
con.commit()
