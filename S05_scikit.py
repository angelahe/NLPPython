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
