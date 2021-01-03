# regular expressions part 1

# pattern identifier
# \d digits
# \w alphanumeric
# \s white space
# \D non digit
# \W non-alphanumeric
# \S non-whitespace
# \d{3} 3 digits

# pattern quantities
# +     occurs one or more times
# {3}   occurs exactly 3 times
# {2,4} occurs 2 to 4 times
# {3,}  occurs 3 or more times
# *     occurs zero or more times
# ?     occurs once or none

# example pattern code
# file_\d\d  matches file_25
# \w-\w\w\w matches A-b_1
# a\sb\sc matches a b c
# \D\D\D matches ABC
# \W\W\W\W\W matches *-+=)
# \S\S\S\S matches Yoyo
# Version \w-\w+
# \D{3} will match with abc
# \d{2,4} will match with 123
# \w{3,} will match anycharacters123
# A*B*C will match AAACC
# ? plurals? will match plural (once or none)

import re

text = 'the phone number is 403-555-1234.  all soon.'
found = '403-555-1234' in text
print (f'{found}')

pattern = 'phone'

# find first instance
my_match = re.search(pattern, text)
# if found, beginning index and end index in the string
print(f'found at index: {my_match.span()}')

my_match.start()
my_match.end()

text2 = 'my phone is a new phone'
match = re.search(pattern, text)
all_matches = re.findall('phone', text2)
print(f'number of matches is {len(all_matches)}')

for match in re.finditer('phone', text2):
    print(match.span())

pattern_phone = r'\d\d\d-\d\d\d-\d\d\d\d'
# could also be...
pattern_phone2 = r'\d{3}-\d{3}-\d{4}'
phone_number = re.search(pattern_phone, text)
print(f'phone number found is: {phone_number.group()} beginning at index {phone_number.start()}')