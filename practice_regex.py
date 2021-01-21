import re
# /<entityname>?$select=[<propertyname>,]*&expand=<entityname>($select=[<propertname>,]*)

text = '/entity?$select=property1,property2,property3'
main_entity_pattern = r'(/)(\w+)(\?\$)'

entity_match = re.search(main_entity_pattern, text)
print(f'found at index: {entity_match.span()}')
print(f'start at index: {entity_match.start()}')
print(f'end at index: {entity_match.end()}')
print(f'the entity name is {entity_match.group(2)}')

# first try:
main_entity_properties_pattern = r'(/\w+\?\$select=)((\w+)(,\w+)*)(&)?'
property_match = re.search(main_entity_properties_pattern, text)
print(f'found I hope: {property_match.span()}')
print(f'found matches 1 to n: {property_match.group(2)}')
