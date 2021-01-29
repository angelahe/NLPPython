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
