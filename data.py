import pandas as pd
import csv
from random import choices

df = pd.read_csv('absurdist_books.csv')
print(df.head())
    
title = df.at[0, 1]
print(title)