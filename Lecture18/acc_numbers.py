#!/usr/bin/python3

# Here's a list of made-up gene accession numbers:
# xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp
# Write a Python programme/script that will print only the accessions that satisfy the following criteria individually (i.e. treat each criterion separately):
# contain the number 5
# contain the letter d or e
# contain the letters d and e in that order
# contain the letters d and e in that order with a single letter between them
# contain both the letters d and e in any order
# start with x or y
# start with x or y and end with e
# contains any 3 numbers in any order
# contains 3 different numbers in the accession
# contain three or more numbers in a row
# end with d followed by either a, r or p

import re

acc_numbers = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

# contain the number 5
for acc_no in acc_numbers:
    match = re.search(r'5', acc_no)
    if match != None:
        print(acc_no)
print(f"{'-'*80}")

# contain the letter d or e
for acc_no in acc_numbers:
    match = re.search(r'(e|d)', acc_no)
    if match != None:
        print(acc_no)
print(f"{'-'*80}")

# contain the letters d and e in that order
for acc_no in acc_numbers:
    match = re.search(r'd.*e', acc_no)
    if match != None:
        print(acc_no)
print(f"{'-'*80}")

# contain the letters d and e in that order with a single letter between them
for acc_no in acc_numbers:
    match = re.search(r'd.e', acc_no)
    if match != None:
        print(acc_no)
print(f"{'-'*80}")

# contain both the letters d and e in any order
print('# contain both the letters d and e in any order')
for acc_no in acc_numbers:
    if re.search(r'd', acc_no) and re.search(r'e', acc_no):
        print(acc_no)
print(f"{'-'*80}")

# start with x or y
for acc_no in acc_numbers:
    match = re.search(r'^[xy]', acc_no)
    if match != None:
        print(acc_no)
print(f"{'-'*80}")
# start with x or y and end with e
print(' start with x or y and end with e')
for acc_no in acc_numbers:
    match = re.search(r'^[xy].*e$', acc_no)
    if match != None:
        print(acc_no)
print(f"{'-'*80}")
# contains any 3 numbers in any order
for acc_no in acc_numbers:
    match = re.search(r'.*\d.*\d.*\d', acc_no) # --------------------Not sure
    if match != None:
        print(acc_no)
print(f"{'-'*80}")
# contains 3 different numbers in the accession
for acc_no in acc_numbers:
    if len(set(re.findall(r'\d',acc_no))) == 3 :
        print(acc_no)
print(f"{'-'*80}")
# contain three or more numbers in a row
for acc_no in acc_numbers:
    match = re.search(r'\d{3}\d*', acc_no)
    if match != None:
        print(acc_no)
print(f"{'-'*80}")
# end with d followed by either a, r or p
print("end with d followed by either a, r or p")
for acc_no in acc_numbers:
    match = re.search(r'd(a|r|p)$', acc_no)
    if match != None:
        print(acc_no)
print(f"{'-'*80}")