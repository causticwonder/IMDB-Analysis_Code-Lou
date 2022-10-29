import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('title.basics.tsv.gz', sep='\t')
print(df.head)

my_list = list(df)
print(my_list)

df2 = df[['tconst', 'primaryTitle']]

df2.to_csv('title_basics.csv')

df3 = pd.read_csv('title.ratings.tsv.gz', sep='\t')
print(df3.head)

df_merge = pd.merge(df2, df3, how = 'inner', on ='tconst')
print(df_merge.head)

my_list2 = list(df_merge)
print(my_list2)

df_merge.to_csv('title_merge.csv')