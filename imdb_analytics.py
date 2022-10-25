import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('title.ratings.tsv.gz', sep='\t') #open tsv.gz files with tab delimiter

print(len(df)) #original dataset size

print(df.shape) #original dataset shape

df_ratings = df['averageRating'].mean() #find average or mean of averageRating column
print(df_ratings)

df_ratings = df.describe()#print all statistics for data
print(df_ratings)

df_votes = df['numVotes'].mean()#average of numVotes column
print(df_votes)

# filter rows with average rating less than 7.5
df_filtered_rating = df[df['averageRating'] >= 7.5]

#filter rows with average number of votes <= 75
df_filtered_votes = df_filtered_rating[df_filtered_rating['numVotes'] <= 75]
 
# Print the new dataframe
print(df_filtered_rating.head(15))
 
# Print the shape of the dataframe
print(df_filtered_rating.shape)

# Print the new dataframe
print(df_filtered_votes.head(15))
 
# Print the shape of the dataframe
print(df_filtered_votes.shape)

sorted_df = df_filtered_votes.sort_values(by=['averageRating'], ascending=False)
print(sorted_df)

df_filtered_votes.plot.hist(x = 'averageRating', y = 'numVotes')

plt.show()# show filtered histogram

df.plot()

