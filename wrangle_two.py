# sets

import random

list_1 = [random.randint(0, 30) for x in range (0, 100)]
list_2 = list(set(list_1))
print(f'the list:\n{list_1}')
print(f'unique numbers:\n{list_2}')