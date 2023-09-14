import re

names = ['Brian Daugette',
         'Veronica Supersonica',
         'Tony Gasparovic',
         'Patrick Germann',
         'm!sha']

regex = '^\w+\s+\w+$'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)

names = ['Brian Daugette',
         'Veronica Supersonica',
         'Tony Gasparovic',
         'Patrick Germann',
         'm!sha']

regex = '^(\w+)\s+(\w+)$'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)
        print(match.group(1))
        print(match.group(2))

names = ['Brian Daugette',
         'Veronica Supersonica',
         'Tony Gasparovic',
         'Patrick Germann',
         'm!sha']

regex = '^(?P<fn>\w+)\s+(?P<ln>\w+)$'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)
        print(match.group('fn'))
        print(match.group('ln'))

names = ['Brian Daugette',
         'Veronica Supersonica',
         'Tony Gasparovic',
         'Patrick Germann',
         'm!sha']

regex = '^[a-zA-Z!]+$'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)

names = ['Brian Daugette',
         'Veronica Supersonica',
         'Tony Gasparovic',
         'Patrick Germann',
         'm!sha']
# scan for blocks of lower case letters
regex = '[a-z]+'
for name in names:
    match = re.findall(regex, name)
    if match:
        print(match)

    matches = re.finditer(regex, name)
    for match in matches:
        print(match)





