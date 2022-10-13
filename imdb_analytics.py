import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('title.ratings.tsv.gz', sep='\t') #open tsv.gz files with tab delimiter

print(len(df)) #original dataset size

print(df.shape) #original dataset shape

# filter rows with average rating less than 7.5
df_filtered_rating = df[df['averageRating'] >= 7.5]

#filter rows with average number of votes <= 75
df_filtered_votes = df_filtered_rating[df_filtered_rating['numVotes'] <= 75]
 
# Print the new dataframe
#print(df_filtered_rating.head(15))
 
# Print the shape of the dataframe
#print(df_filtered_rating.shape)

# Print the new dataframe
print(df_filtered_votes.head(15))
 
# Print the shape of the dataframe
print(df_filtered_votes.shape)

df_filtered_votes.plot.hist(x = 'averageRating', y = 'numVotes')

plt.show()

