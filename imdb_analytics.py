import pandas as pd #import pandas
import matplotlib.pyplot as plt

df = pd.read_csv('title.ratings.tsv.gz', sep='\t') #open tsv.gz files with tab delimiter

print(df.head())

print(len(df))

df.plot.scatter(x = 'averageRating', y = 'numVotes')

plt.show()

