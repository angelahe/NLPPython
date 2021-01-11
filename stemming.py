import nltk

from nltk.stem.porter import PorterStemmer

p_stemmer = PorterStemmer()

words = ['run', 'runner', 'ran', 'runs', 'easily', 'fairly', 'fairness']

for word in words:
    print(word + '---->' + p_stemmer.stem(word))

# slightly better stemmer - snowball
from nltk.stem.snowball import SnowballStemmer

s_stemmer = SnowballStemmer(language='english')
print('\nUsing snowball stemmer:')
for word in words:
    print(word + '----> ' + s_stemmer.stem(word))

words2 = ['generous', 'generation', 'generously', 'generate']
print('\nAnother example of snowball stemming:')
for word in words2:
    print(word + '---->' + s_stemmer.stem(word))