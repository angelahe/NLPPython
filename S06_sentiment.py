# VADER Valence Aware Dictionary for Sentiment Reasoning in NLTK
# sensitive to polarity (positive/negative) and intensity
# doesn't deal well with both positive and negative
# doesn't handle sarcasm

import nltk
# only need to download this once
# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

a = 'This is a good movie'
print(a)
print(f'polarity scores: {sid.polarity_scores(a)}')

b = 'This was the best, mos awesome movie EVER MADE!!!'
print(b)
print(f'polarity scores: {sid.polarity_scores(b)}')

c = 'This was the WORST movie tht is ever disgraced the screen.'
print(c)
print(f'polarity scores: {sid.polarity_scores(c)}')

import pandas as pd

df = pd.read_csv('material/UPDATED_NLP_COURSE/TextFiles/amazonreviews.tsv',sep='\t')
print(df.head())
df['label'].value_counts()

# clean the data a little
blanks = []
df.dropna(inplace=True)
for i, label, review in df.itertuples():
    if type(review) == str:
        if review.isspace():
            blanks.append(i)

df.drop(blanks,inplace=True)

print(df.iloc[0]['review'])

print(sid.polarity_scores(df.loc[0]['review']))

# adding scores and labels to the dataframe
df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))

print(df.head())

df['compound']  = df['scores'].apply(lambda score_dict: score_dict['compound'])

print(df.head())

df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >=0 else 'neg')

print(df.head())

# compare label with the computed compound score
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

print(f"accuracy score: {accuracy_score(df['label'],df['comp_score'])}")

print(classification_report(df['label'],df['comp_score']))

print(confusion_matrix(df['label'],df['comp_score']))
