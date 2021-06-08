#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attemp = 5
while pw != secret:
    count += 1
    if count > max_attemp:
        break
    pw = input(f'{count}:What\'s the secret word? ')
else:
    auth = True
    
print('Authorized' if auth else 'call the FBI...')