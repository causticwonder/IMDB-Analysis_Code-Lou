import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('title.ratings.tsv.gz', sep='\t') #open tsv.gz files with tab delimiter

df2 = pd.read_csv('title_basics.csv.gz') #open title csv.gz file 

df_merge = pd.merge(df, df2, how = 'inner', on ='tconst')
print(df_merge.head)

my_list = list(df_merge)
print(my_list)

print(len(df_merge)) #original dataset size

print(df_merge.shape) #original dataset shape

df_ratings = df_merge['averageRating'].mean() #find average or mean of averageRating column
print(df_ratings)

df_ratings = df_merge.describe()#print all statistics for data
print(df_ratings)

df_votes = df_merge['numVotes'].mean()#average of numVotes column
print(df_votes)

# filter rows with average rating less than 7.5
df_filtered_rating = df_merge[df_merge['averageRating'] >= 7.5]

#filter rows with average number of votes <= 75
df_filtered_votes = df_filtered_rating[df_filtered_rating['numVotes'] <= 75]
 
# Print the new dataframe
print(df_filtered_votes.head(15))
 
# Print the shape of the dataframe
print(df_filtered_votes.shape)

sorted_df = df_filtered_votes.sort_values(by=['averageRating'], ascending=False)
print(sorted_df)

plt.hist(sorted_df['averageRating'], bins=[7,8,9,10])

plt.title('Average Rating by Number of Votes')
plt.ylabel('Number of Votes')
plt.xlabel('Average Rating')
plt.show() # show filtered histogram




