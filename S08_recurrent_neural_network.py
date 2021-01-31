# examples of sequences
# time series
# sentences
# audio
# car trajectories
# music

# recurrent neuron - sends output back to itself

# LSTM and GRU and Text Generation
# LSTM - long short term memory to deal with forgetting earlier training
# peephole LSTM
# GRU - gated recurrent unit - combine the forget and input gates into update gate
# depth first gated

# will use this for LSTM text generation

# note this workaround for an error complaining of multiple copies of libiomp5.dylib being linked
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# process text
# clean text
# tokenize text and create sequences with Keras

def read_file(filepath):

    with open(filepath) as f:
        str_text = f.read()

    return str_text

import spacy
nlp = spacy.load('en',disable=['parser', 'tagger','ner'])

# may need to make the length longer
nlp.max_length = 1198623

def separate_punc(doc_text):
    return [token.text.lower() for token in nlp(doc_text) if token.text not in '\n\n \n\n\n!"-#$%&()--.*+,-/:;<=>?@[\\]^_`{|}~\t\n ']

d = read_file('material/UPDATED_NLP_COURSE/06-Deep-Learning/moby_dick_four_chapters.txt')

# for whole book:
# d = read_file('material/UPDATED_NLP_COURSE/06-Deep-Learning/melville-moby_dick.txt')
tokens = separate_punc(d)
print(f'number of tokens in 1st 4 chapters: {len(tokens)}')

# read in first 25 words of a sentence and have the model predict the 26th word

# organize into sequences of tokens
train_len = 25 + 1
# empty list of sequences
text_sequences = []

for i in range(train_len, len(tokens)):
    # grab tren_len number of tokens
    seq = tokens[i-train_len:i]
    # Add to list of sequences
    text_sequences.append(seq)

print(f'first text sequence: {text_sequences[0]}')

print('show sequence + next word')
print(' '.join(text_sequences[0]))
print('show sequence shifted over 1 word')
print(' '.join(text_sequences[1]))
print('show sequence shifted over 2 words')
print(' '.join(text_sequences[2]))

# Keras tokenization

from keras.preprocessing.text import Tokenizer
# integer encode sequences of words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_sequences)
sequences = tokenizer.texts_to_sequences(text_sequences)

print('tokens of sequences first sequence replaced with numbers ie id of a word: {sequences[0]')
print('mapping of token to word:')
print(tokenizer.index_word)

print('token mapping to words for first sequence')
for i in sequences[0]:
    print(f'{i} : {tokenizer.index_word[i]}')

print(f'word count for first 4 chapters: {tokenizer.word_counts}')
vocabulary_size = len(tokenizer.word_counts)

# convert to numpy matrix
import numpy as np
sequences = np.array(sequences)
# each row represents a single line in the text, all shifted over by one word for the next sequence
# ie there are as many sequences as there are words in the document
print(sequences[:5])

# features labels split
from keras.utils import to_categorical
# grab all but last word from each sequence row
X = sequences[:,:-1]
# grab last word from each sequence row
y = sequences[:,-1]
# change y into a to_categorical
y = to_categorical(y, num_classes=vocabulary_size+1)
seq_len = X.shape[1]

# create LSTM based model
from keras.models import Sequential
from keras.layers import Dense,LSTM,Embedding

def create_model(vocabulary_size, seq_len):
    model = Sequential()
    model.add(Embedding(vocabulary_size, 25, input_length=seq_len))
    model.add(LSTM(150, return_sequences=True))
    model.add(LSTM(150))
    model.add(Dense(150, activation='relu'))

    model.add(Dense(vocabulary_size, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    print(model.summary())

    return model

model = create_model(vocabulary_size+1, seq_len)

# save the model then fit the model for training

from pickle import dump,load
# fit model
model.fit(X, y, batch_size=128, epochs=300,verbose=1)

# save the model to file
model.save('epochBIG.h5')
# save the tokenizer
dump(tokenizer, open('epochBIG', 'wb'))