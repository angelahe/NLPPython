# movie review dataset - determine if positive or negative review
import numpy as np
import pandas as pd

df = pd.read_csv('material/UPDATED_NLP_COURSE/TextFiles/moviereviews.tsv', sep='\t')
print(df.head())

# the first review
print(df['review'][0])

# raw number
print(f'number of reviews before check for empty and null: {len(df)}')
# check for and remove empty reviews
df.isnull().sum()

df.dropna(inplace=True)

mystring = 'hello'
empty = '   '
print(f'mystring empty? {mystring.isspace()}')
print(f'empty is empty? {empty.isspace()}')

# remove empty strings too
blanks = []
# index, label, review text
for i, lb, rv in df.itertuples():
    if rv.isspace():
        blanks.append(i)
# now that have index positions of blank reviews can drop them
df.drop(blanks, inplace=True)
print(f'number of valid reviews is now: {len(df)}')