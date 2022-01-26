import pandas as pd

df = pd.read_csv('summary.txt', sep='\n')
df.to_excel('summary.xlsx', 'Sheet1')


