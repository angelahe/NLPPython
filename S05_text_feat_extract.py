# build a vocabulary

vocab = {}
i = 1

with open('material/UPDATED_NLP_COURSE/03-Text-Classification/1.txt') as f:
    x = f.read().lower().split()

for word in x:
    if word in vocab:
        continue
    else:
        vocab[word] = i
        i+=1

print(vocab)

with open('material/UPDATED_NLP_COURSE/03-Text-Classification/2.txt') as f:
    x = f.read().lower().split()

for word in x:
    if word in vocab:
        continue
    else:
        vocab[word] = i
        i+=1

print(vocab)

# create empty vector with space for each word in vocab
one = ['1.txt']+[0]*len(vocab)
print(one)

#map the frequencies of each word to the vector
with open('material/UPDATED_NLP_COURSE/03-Text-Classification/1.txt') as f:
    x = f.read().lower().split()

for word in x:
    one[vocab[word]]+=1

print(f'frequency list 1: {one}')

two = ['2.txt']+[0]*len(vocab)
print(two)

#map the frequencies of each word to the vector for doc 2
with open('material/UPDATED_NLP_COURSE/03-Text-Classification/2.txt') as f:
    y = f.read().lower().split()

for word in y:
    two[vocab[word]]+=1

print(f'frequency list 2: {two}')




print(one)
print(two)