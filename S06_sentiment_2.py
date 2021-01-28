import numpy as np
import pandas as pd

df = pd.read_csv('material/UPDATED_NLP_COURSE/TextFiles/moviereviews.tsv', sep='\t')
df.head()
df.dropna(inplace=True)

blanks = []  # start with an empty list

for i,lb,rv in df.itertuples():  # iterate over the DataFrame
    if type(rv)==str:            # avoid NaN values
        if rv.isspace():         # test 'review' for whitespace
            blanks.append(i)     # add matching index numbers to the list

df.drop(blanks, inplace=True)

print(df['label'].value_counts())

#import sentiment analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


sid = SentimentIntensityAnalyzer()

# use sid to append a comp_score to the dataset
df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))

df['compound']  = df['scores'].apply(lambda score_dict: score_dict['compound'])

df['comp_score'] = df['compound'].apply(lambda c: 'pos' if c >=0 else 'neg')

print(df.head())

# perform comparison analysis across whole dataset
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

print(f"accuracy score: {accuracy_score(df['label'],df['comp_score'])}")

print(classification_report(df['label'],df['comp_score']))

print(confusion_matrix(df['label'],df['comp_score']))

# does poorly because save the judgement until the last, and can't detect sarcasm
