# IMDB-Analysis_Code-Lou

I downloaded the IMDB datasets to analyze in hopes of finding "Hidden Gems" movies, or movies that have a high average score but not a lot of individual ratings. 

Feature 1: Read in data from a local csv, excel file, json, or any other file type. 

What I Did: I pulled tsv.gz data from IMDB's dataset and read into VS Code using pd.read. 

Feature 2: Use custom functions or lambdas to perform specific operations to clean or manipulate your data, return those values, then use them in other parts of your project.

What I Did:  In a separate python file, title_extract.py, using Pandas - I extracted two specific columns (identifier number and title) from a giant IMDB dataset file and created a second csv file: title_basics.csv. This new CSV file is still to big to upload to GitHub, so I used the gzip module to compress it down to a smaller file size. I then merged this new DF into my initial dataset (ratings) and used this new, slightly smaller dataset for my analysis. 

Feature 3: Do 5 basic calculations with Pandas, like finding the sum(), median(), mean(), or mode() of a column. You could divide two columns by each other. You could multiple a column by a random integer. You could use string operations and find the most common letter in a given entry. 

What I Did: 
1. Using the len function found the length of my dataframe, 1238396. Which is way more than I expected to be working with initially. 
2. I used Dataframe Describe method to pull the statistics of the data. 
3. Then I found the average score from the averageRatings column, which is approx. 6.94. 
4. I also found the average number of votes, which gets us about 1041 votes per movie. This will help me analyze my data by knowing what to filter out. Any movies with more than 1000 votes will be excluded from the final dataset and any movies that scored under 7.5 will also be excluded. 
5. I sorted the averageRatings column by Descending order. 
6. 1000 votes is WAY too many so I changed the number of exclusion to 75. That still gives me 352824 lines of data to work with. 

Feature 4: Make 2 basic plots with matplotlib, seaborn, or any other kind of visualization library that you think looks interesting.

What I Did: Created a histogram of all AverageRatings and NumVotes data points. 

Feature 5: If using some format other than a notebook, make sure your README explains your project. 

What I Did: This README is my vague attempt at explaining my project/thought process. I have no idea what I'm doing and I'm making it up as I go, but that pretty much explains my entire journey through adulthood, so why not. 

