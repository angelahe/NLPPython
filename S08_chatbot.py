# Q & A chatbot
# see https://arxiv.org/pdf/1503.08895.pdf
# for the detailed research

# load the data
import pickle
import numpy as np

with open("material/UPDATED_NLP_COURSE/06-Deep-Learning/train_qa.txt", "rb") as fp:   # Unpickling
    train_data =  pickle.load(fp)

with open("material/UPDATED_NLP_COURSE/06-Deep-Learning/test_qa.txt", "rb") as fp:   # Unpickling
    test_data =  pickle.load(fp)

# explore the data
print(f'trained data has {len(train_data)} and test has {len(test_data)} rows')

print(f'first training data: story, question, answer {train_data[0]}')

print(' '.join(train_data[0][0]))

print(' '.join(train_data[0][1]))

print(train_data[0][2])

# set up vocabulary of the words

# Create a set that holds the vocab words
vocab = set()
all_data = test_data + train_data

for story, question , answer in all_data:
    # In case you don't know what a union of sets is:
    # https://www.programiz.com/python-programming/methods/set/union
    vocab = vocab.union(set(story))
    vocab = vocab.union(set(question))

vocab.add('no')
vocab.add('yes')

print(f'vocab of the story is: {vocab}')

vocab_len = len(vocab) + 1 #we add an extra space to hold a 0 for Keras's pad_sequences

max_story_len = max([len(data[0]) for data in all_data])

print(f'max story length: {max_story_len}')

max_question_len = max([len(data[1]) for data in all_data])

print(f'max question length: {max_question_len}')

# vectorize the data
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

# integer encode sequences of words
tokenizer = Tokenizer(filters=[])
tokenizer.fit_on_texts(vocab)

print(f'tokenizer object: word number index and lowercased: {tokenizer.word_index}')

train_story_text = []
train_question_text = []
train_answers = []

for story,question,answer in train_data:
    train_story_text.append(story)
    train_question_text.append(question)
    train_answers.append(answer)

train_story_seq = tokenizer.texts_to_sequences(train_story_text)

# train story test
def vectorize_stories(data, word_index=tokenizer.word_index, max_story_len=max_story_len,max_question_len=max_question_len):
    '''
    INPUT:

    data: consisting of Stories,Queries,and Answers
    word_index: word index dictionary from tokenizer
    max_story_len: the length of the longest story (used for pad_sequences function)
    max_question_len: length of the longest question (used for pad_sequences function)


    OUTPUT:

    Vectorizes the stories,questions, and answers into padded sequences. We first loop for every story, query , and
    answer in the data. Then we convert the raw words to an word index value. Then we append each set to their appropriate
    output list. Then once we have converted the words to numbers, we pad the sequences so they are all of equal length.

    Returns this in the form of a tuple (X,Xq,Y) (padded based on max lengths)
    '''


    # X = STORIES
    X = []
    # Xq = QUERY/QUESTION
    Xq = []
    # Y = CORRECT ANSWER
    Y = []


    for story, query, answer in data:

        # Grab the word index for every word in story
        x = [word_index[word.lower()] for word in story]
        # Grab the word index for every word in query
        xq = [word_index[word.lower()] for word in query]

        # Grab the Answers (either Yes/No so we don't need to use list comprehension here)
        # Index 0 is reserved so we're going to use + 1
        y = np.zeros(len(word_index) + 1)

        # Now that y is all zeros and we know its just Yes/No , we can use numpy logic to create this assignment
        #
        y[word_index[answer]] = 1

        # Append each set of story,query, and answer to their respective holding lists
        X.append(x)
        Xq.append(xq)
        Y.append(y)

    # Finally, pad the sequences based on their max length so the RNN can be trained on uniformly long sequences.

    # RETURN TUPLE FOR UNPACKING
    return (pad_sequences(X, maxlen=max_story_len),pad_sequences(Xq, maxlen=max_question_len), np.array(Y))

inputs_train, queries_train, answers_train = vectorize_stories(train_data)
inputs_test, queries_test, answers_test = vectorize_stories(test_data)

print(f"index of yes: {tokenizer.word_index['yes']}")
print(f"index of no: {tokenizer.word_index['no']}")


