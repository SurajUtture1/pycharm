import re

values = ['https://www.socratica.com',
          'https://www.socratica.org',
          'file://test.this.path',
          'com.socratica.www_https://'
          ]
# Test if a string starts with http or https
regex = 'https?'
for value in values:
    if re.match(regex, value):
        print(value)

values = ['https://www.socratica.com',
          'https://www.socratica.org',
          'file://test.this.path',
          'com.socratica.www_https://'
          ]

regex = 'https?://w{3}.\w+.(org|com)'
for value in values:
    if re.fullmatch(regex, value):
        print(value)
