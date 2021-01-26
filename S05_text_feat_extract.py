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