# IMDB-Analysis_Code-Lou

I downloaded the IMDB datasets to analyze in hopes of finding "Hidden Gems" movies, or movies that have a high average score but not a lot of individual ratings. All datasets can be found at https://datasets.imdbws.com/

Technical Instructions: Modules needed to run:  pandas, matplotlib.plotly,

Feature 1: Read in data from a local csv, excel file, json, or any other file type. 

What I Did: I pulled two separate tsv.gz data from IMDB's dataset and read into VS Code using pandas pd.read. 

Feature 2: Use custom functions or lambdas to perform specific operations to clean or manipulate your data, return those values, then use them in other parts of your project.

What I Did:  Filtered the title basics dataframe to only include specific columns - the identifier column (tconst), titleType, and primaryTitle columns. Then created another df to exclude any rows where the titleType was not a movie. This eliminates a large portion of the dataset. 
I created a third dataframe merging the newly filtered dataframe with the IMDB ratings dataset. This gives me all the data I actually want to analyze. 

Feature 3: Do 5 basic calculations with Pandas, like finding the sum(), median(), mean(), or mode() of a column. You could divide two columns by each other. You could multiple a column by a random integer. You could use string operations and find the most common letter in a given entry. 

What I Did: 
1. Using the len function found the length of my dataframe, 282304. Which is way more than I expected to be working with initially. 
2. I used Dataframe Describe method to pull the statistics of the data. 
3. Then I found the average score from the averageRatings column, which is approx. 6.18. 
4. I also found the average number of votes, which gets us about 3561 votes per movie. This will help me analyze my data by knowing what to filter out. Any movies with more than 75 votes will be excluded from the final dataset and any movies that scored under 7.5 will also be excluded. 
5. I sorted the averageRatings column by Descending order because I like orderly data :) 

Feature 4: Make 2 basic plots with matplotlib, seaborn, or any other kind of visualization library that you think looks interesting.

What I Did: 

1.Using matplotlib, I created a histogram of all AverageRatings and NumVotes data points. 
2.Using matplotlib, I created a scatterplot of all the same data. 

Feature 5: If using some format other than a notebook, make sure your README explains your project. 

What I Did: This README is my vague attempt at explaining my project/thought process. I have no idea what I'm doing and I'm making it up as I go, but that pretty much explains my entire journey through adulthood, so why not. 
I also added md cells between the code to hopefully explain the work/process/confusion a little better. 

