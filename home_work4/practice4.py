import pandas as pd
import numpy as np

database = pd.read_csv('tested.csv')
#1.1
print(database.isnull().sum())
print("=================================")
#1.2
print(database.info())
print("=================================")
#1.3

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(database.head())
print("=================================")
#1.4
print(database["Age"].mean())
print(database["Age"].max())
print(database["Age"].min())
print(database["Age"].median())
print(database["Age"].std())
print("====================================")
#1.5
column_list = database.columns.tolist()
print(f'Колво заголовков - {len(column_list)}')
row_list = len(database)
print(f'Колво строк - {row_list}')