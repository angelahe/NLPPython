# simple data wrangling techniques

list_example = [51, 27, 34, 46, 90, 45, -19]

list_example2 = [15, "Yellow car", True, 9.456, [12, "Hello"]]

# ex 1
list_1 = [34, 12, 89, 1]
print(f'the list: {list_1}')
# access using forward index
print(f'first in the list: {list_1[0]}')
print(f'last in the list: {list_1[3]}')
print(f'last in the list: {list_1[len(list_1)-1]}')
# list slicing
print(f'get 2nd and 3rd in list: {list_1[1:3]}')
# using backward indices
print(f'last in the list: {list_1[-1]}')
print(f'get last 2 in list: {list_1[-2:]}')
print(f'get 1st 2 in list: {list_1[:-2]}')
# using : go to the end or the beginning
# reverse elements, not very readable
print(f'elements reversed: {list_1[-1::-1]}')