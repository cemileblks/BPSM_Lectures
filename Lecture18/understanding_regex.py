#!/usr/bin/python

import re
import string
test_string = '123abc456789abc123ABC'

matches_finditer = re.finditer(r'abc', test_string)

print(matches_finditer)
print(type(matches_finditer)) # callable iterator object

# for match in matches_finditer:
#     print(match)
#     print(type(match)) # match object if found 

matches_findall = re.findall(r'abc', test_string)
print(matches_findall)
print(type(matches_findall)) # list

matches_match = re.match(r'123', test_string)
print(matches_match)
print(type(matches_match)) # Match obj or none type

match_search = re.search(r'abc', test_string)
print(match_search) # Match obj or none type

#===========================================================

# Methods of the re.Match object
# group, start, end, span
for match in matches_finditer:
    print(match.span()) # gives the span of each find start end end postions
    print(match.start()) # gives start pos
    print(match.end()) # gives end pos
    print(match.group()) # print the re match string, also group(0)

print(f"\n{'-'*80}\n")

my_string = 'Cemile Balkas 2002 Camille_Cemile'

my_alphabet = string.ascii_lowercase

second_matches = re.finditer(r'CEMILE', my_string, re.I)
print(second_matches)

for match in second_matches:
    print(match)


some_sentence1 = '1353abcABCDEFabcPYTHON'
splitted_sentence = re.split(r"abc", some_sentence1) # splits out to list  
print(splitted_sentence)

some_sentence = "Hello WORLd you are the best wOrld"
subbed_string = re.sub(r"world", "planet", some_sentence, flags=re.IGNORECASE) # replaces the finds

print(subbed_string)


text = "$23.45 $400"
matches = re.findall(r'\$\d+(?:\.\d{2})?', text)
print(matches)

matches_numbers_finditer = re.finditer(r'\$\d+(\.\d{2})?', text)
for match in matches_numbers_finditer:
    print(match)
