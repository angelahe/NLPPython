import re

#compile separate groups by using parentheses

text = 'Annie phone number is 888-555-1234'
pattern = r"(\d{3})-(\d{3})-(\d{4})"
mymatch = re.search(pattern, text)
print(f'area code is {mymatch.group(1)}')

# pipe for or statement
mymatch2 = re.search(r"man|woman", "This man was here")
print(f'found man or woman in string? {mymatch2.group()}')

# or use wildcard match
print(f'strings ending with at: {re.findall(r".at", "The cat in the hat sat")}')

# other patterns
# ^ starts with e.g. r"^\d", '1 is the loneliest number'
# $ ends with e.g. r"$\d, 'this string has 2'

# get rid of all numbers using [ for exclusion and then reassemble to string by +
phrase = "there are 3 numbers 34 inside 5 this sentence"
mymatch3 = re.findall(r"[^\d]+", phrase)
print(f'removed numbers: {mymatch3}')

# remove punctuation
test_phrase = "this is a string! but it has punctuation. How to remove it?"
mylist = re.findall(r"[^!.? ]+", test_phrase)
print(f'list of all without punctuation or whitespace: {mylist}')

# join the tokens back together with spaces
mystring = ' '.join(mylist)
print(f'now as a string: {mystring}')

# grab group of alphanumerics [\w]+
text = "Only find the hyphen-words. Where are the long-ish dash words"
findhyphens = re.findall(r'[\w]+-[\w]+', text)
print(f'these are the hyphen words {findhyphens}')