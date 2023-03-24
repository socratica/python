# Topics:
#   - Quick overview of regexes
#   - match,  search,  findall,  split,  sub

# Group 1:  Fracois, Mike Whitney, Sagun Khatri, Nick Francesco, Pickles, K5ANR
# Group 2:  HappyCodingRobot, Finn Bindeballe, Ron Cromberge, Geir Anders Berge
# Group 3:  Brian Daugette, Veronica Supersonica, Tony Gasparovic, Patrick Germann, m!sha

import re

names1 = ['Fracois', 'Mike Whitney', 'Sagun Khatri',
          'Nick Francesco', 'Pickles', 'K5ANR']

names2 = ['HappyCodingRobot', 'Finn Bindeballe', 'Ron Cromberge',
          'Geir Anders Berge', 'Sohil']

names3 = ['Brian Daugette', 'Veronica Supersonica',
          'Tony Gasparovic', 'Patrick Germann', 'm!sha']

paths = ['https://www.socratica.com',
         'http://www.socratica.org',
         'file://test.this.path',
         'com.socratica.www_https://']

# Using the match function
# regex = 'https?://'
# for path in paths:
#     if re.match(regex, path):
#         print(path)

# Use the fullmatch function
# regex = 'https?://w{3}\.\w+\.(org|com)'
# for path in paths:
#     if re.fullmatch(regex, path):
#         print(path)

names = names3
regex = '^(\w+)\s+(\w+)$'
for name in names:
    match = re.search(regex, name)
    if match:
        print()
        print(match.group())
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))