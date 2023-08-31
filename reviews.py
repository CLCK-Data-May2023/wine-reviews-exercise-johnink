# add your code here
import pandas as pd

reviews = pd.read_csv('data\winemag-data-130k-v2.csv.zip', index_col=0)

reviews_country = reviews.groupby(['country']).points.agg([count,mean])

with open('data\\reviews-per-country.csv', 'w') as csv_file:
    reviews_country.to_csv(path_or_buf=csv_file)

