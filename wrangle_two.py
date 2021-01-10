# sets

import random

list_1 = [random.randint(0, 30) for x in range (0, 100)]
list_2 = list(set(list_1))
print(f'the list:\n{list_1}')
print(f'unique numbers:\n{list_2}')

set1 = {"Apple", "Orange", "Banana"}
set2 = {"Pear", "Peach", "Mango", "Banana"}

union_set = set1 | set2
print(f'set1: {set1}\n + set2:{set2}')
print(f'union of sets: {union_set}')
intersection_set = set1 & set2
print(f'intersection: {intersection_set} ')

# create null set
null_set_1 = set({})

# create a dictionary
null_dictionary = {}

# create a dictionary (keys must be unique)
dict_1 = {"key1": "value1", "key2": "value2"}
print(f'dictionary: {dict_1}')

dict_2 = {"key1": 1, "key2": ["list_element1", 34], "key3": "value3", "key4": {"subkey1": "v1"}, "key5": 4.5}
print(f'also a dictionary: {dict_2}')

# ex 6 access and set values in dictionary
# access a key
print(f'key2 in 2nd dict: {dict_2["key2"]}')

# assign a new value to a key
dict_2["key2"] = "My new value"

#define blank dictionary then assign values to it
dict_3 = {}
dict_3["key1"] = "value1"
print(f'new dictionary: {dict_3}')

# ex 7 iterating over a dictionary
dict_4 = {"key1": 1, "key2": ["list_element1", 34], "key3": "value3", "key4": {"subkey1": "v1"}, "key5": 4.5}
for k, v in dict_4.items():
    print("{} - {}".format(k, v))

