import pickle
import pandas as pd
import gzip
 
df = pd.read_csv('title_basics.csv')
 
# write a pandas dataframe to gzipped CSV file
df.to_csv("title_basics.csv.gz", 
           index=False, 
           compression="gzip")