# bag of words, stop words and stems, tagging
import numpy as np
import pandas as pd

df = pd.read_csv('material/UPDATED_NLP_COURSE/TextFiles/smsspamcollection.tsv', sep='\t')
print(df.head)

# check for null values
print(df.isnull().sum())

print(df['label'].value_counts())

# split data into data set and training set
from sklearn.model_selection import train_test_split

X = df['message']  # this time we want to look at the text
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

#fit vectorizer to the data
# count_vect.fit(X_train)
#transform the original text message to vector
# X_train_counts = count_vect.transform(X_train)

# or use the convenience method since you usually do fit then transform
X_train_counts = count_vect.fit_transform(X_train)
# compress using the zeros, is a large matrix, don't print!!
print(X_train.shape)
print(X_train_counts.shape)