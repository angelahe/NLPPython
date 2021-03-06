import numpy as np
import pandas as pd

# pandas read in csv as data frame object

df = pd.read_csv('material/UPDATED_NLP_COURSE/TextFiles/smsspamcollection.tsv',sep='\t')
# show first 5 rows
print(df.head())

# if anything missing will catch it
print(df.isnull().sum())
print(f'length of tsv: {len(df)}')

print(f'unique values in label column:')
print(df['label'].unique())
print(f"counts of the values: \n{df['label'].value_counts()}")

import matplotlib.pyplot as plt

#distribution of spam vs ham by length of text, longer tend to be spam
plt.xscale('log')
bins = 1.15**(np.arange(0,50))
plt.hist(df[df['label']=='ham']['length'],bins=bins,alpha=0.8)
plt.hist(df[df['label']=='spam']['length'],bins=bins,alpha=0.8)
plt.legend(('ham','spam'))
plt.show()

# distribution of spam vs ham with punctuation, not as distinct
plt.xscale('log')
bins = 1.5**(np.arange(0,15))
plt.hist(df[df['label']=='ham']['punct'],bins=bins,alpha=0.8)
plt.hist(df[df['label']=='spam']['punct'],bins=bins,alpha=0.8)
plt.legend(('ham','spam'))
plt.show()

from sklearn.model_selection import train_test_split

# X feature data
X = df[['length', 'punct']]
# y label
y = df['label']
# 30% test set, random_state for repeatable test
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)

#show rows and columns of the data
print(f'X_train is: {X_train.shape}')

print(f'X_test is: {X_test.shape}')

from sklearn.linear_model import LogisticRegression

# create instance of regression model
lr_model = LogisticRegression(solver='lbfgs')

# fit the model to the training data
# pass in training data and the labels
print(f'{lr_model.fit(X_train, y_train)}')

# now the model is ready to predict
from sklearn import metrics
predictions = lr_model.predict(X_test)
print(f'predictions: {predictions}')

# not predicting well on spam
print(metrics.confusion_matrix(y_test, predictions))

# test the accuracy of the model
df = pd.DataFrame(metrics.confusion_matrix(y_test,predictions), index=['ham','spam'], columns=['ham','spam'])
# print confusion matrix
#  true positive  | false positive
#  false negative | true negative
print(df)

#print classification report for precision, recall and f1 score for each category
print(metrics.classification_report(y_test, predictions))

#overall accuracy
print('overall accuracy')
print(metrics.accuracy_score(y_test, predictions))

# run using other algorithm - this one doesn't do well with spam at all
from sklearn.naive_bayes import MultinomialNB

# these five steps are the pattern regardless of the algorithm
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
predictions = nb_model.predict(X_test)
print(metrics.confusion_matrix(y_test, predictions))
print(metrics.classification_report(y_test, predictions))

from sklearn.svm import SVC

svc_model = SVC()
svc_model.fit(X_train, y_train)
predictions = svc_model.predict(X_test)
print(metrics.confusion_matrix(y_test, predictions))
print(metrics.classification_report(y_test, predictions))