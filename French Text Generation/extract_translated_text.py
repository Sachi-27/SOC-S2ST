import csv
import pandas as pd

data = pd.read_csv("all_text_translated_all_text.csv")

print(data.columns)
translated_data = data['FR']
# print(len(translated_data))

translated_data.to_csv('translated_text.csv', index=False)

