# simple data wrangling techniques

list_example = [51, 27, 34, 46, 90, 45, -19]

list_example2 = [15, "Yellow car", True, 9.456, [12, "Hello"]]

# ex 1 accessing list members

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
# reverse elements, not very readable, do not use
print(f'elements reversed: {list_1[-1::-1]}\n')

# ex 2 generate a list
list_2 = []
for x in range(0, 10):
    list_2.append(x)
print(f'list of 10 numbers: {list_2}')

list_3 = [x for x in range(0, 100)]
print(f'list of numbers in range:\n{list_3}')

i = 0
print('iterate over the list to print:\n')
while i < len(list_3) :
    print(list_3[i])
    i += 1

list_4 = [x for x in range(0, 100) if x %5 == 0]
print(f'list of numbers up to 100 in increments of 5:\n {list_4}')


list_a = [1, 4, 56, -1]
list_b = [1, 39, 245, -23, 0, 45]
list_c = list_a + list_b
print(f'add two lists together:\n{list_a} + {list_b} = {list_c}')

list_a.extend(list_b)
print(f'append 2nd list to 1st list using extend:\n{list_a}')

# ex 3 iterate over a list to check membership

list_d = [x for x in range(0, 100)]
for i in range(0, len(list_d)):
    print(list_d[i])

# better iteration over list
for i in list_d:
    print(i)

# check for membership in a list:
print(f'25 in list? {25 in list_d}')
print(f'-45 in list_d? {-45 in list_d}')