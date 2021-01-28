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

