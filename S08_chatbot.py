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

