from datetime import datetime

# print functions
# prints my name is Jose (string variable)
person = "Jose"
print(f"my name is {person}")


# prints my number is 123 (element in a list)
d = {'a':123, 'b':456}
print(f"my number is {d['a']}")

# prints my  number is 0 (element in an array)
mylist = [0, 1, 2]
print(f"my  number is {mylist[0]}")

#alignments and padding
library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting in water alone', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]
for book in library:
    print(f"{book}")
for book in library:
    print(f"Author is {book[0]}")

# tuple unpacking
for author, topic, pages in library:
    print(f"Author is {author}")

# tuple unpacking to print all 3 fields
for author, topic, pages in library:
    print(f"{author} {topic} {pages}")

# tuple unpack with min number of spaces taken by variable
for author, topic, pages in library:
    print(f"{author:10} {topic:30} {pages:->10}")

today = datetime(year=2019, month=2, day=28)
print(f"{today}")
print(f"{today:%B %d, %Y}")

# read from a file, default is read only
myfile = open('test.txt')
myfile.read()
myfile.seek(0)
content = myfile.read()
print(content)
myfile.close()

# iterate lines
myfile = open('test.txt')
mylines = myfile.readlines()
print('\nanother way to print the lines in a file\n')
for line in mylines:
    print(line)

myfile.close()

# write to a file, performs a truncation on the original, only use when intend to completely overwrite the file
# myfile = open('test.txt', 'w+')
# myfile.write('My brand new text')
myfile.close()

myfile = open('test.txt', 'a+')
myfile.write('\nadding a third line')

myfile.close()

# better to use context manager to autoclose the file
with open('test.txt', 'r') as mynewfile:
    myvariable = mynewfile.readlines()
    for line in myvariable