import re

names = ['Finn Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil']

# Find the people with first and last name only, with single white space , skip the peoples with 3 or more names
regex = '^\w+ \w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name)

names = ['Finn   Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron   Cromberge',
         'Sohil']

regex = '^\w+ \w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name)
# result = no word contain single white space


names = ['Finn   Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron   Cromberge',
         'Sohil']

regex = '^\w+\s+\w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name)

names = ['Finn Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil']

regex = '^\w+ \w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(result)

names = ['Finn Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil']

# names starts with C
regex = 'C\w*'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)
        print(match.start())
        print(match.end())
        print(match.span())
        print(match.group())  # this is for if you want to match the substring to regex ## Output = Cromberge



