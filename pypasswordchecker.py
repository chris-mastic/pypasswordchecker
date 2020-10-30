#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 04:34:16 2020

@author: tech

checks if password has ever been hacked.
Although this is setup to be  used from the CL you should probably read for
a temp  text file or come up with some other way to input passwords to program.
A keylogger or other software can see and/or memorize your  keystrokes, e.g.,
CL recall.  This is not  very secure.

"""
import requests
import hashlib
import sys

#kind of like having a browser w/o having a browser
#the api uses hashed passwords not plain text (sha1)
#The api uses k anonymity allows someone to receive info about us w/o them knowing
#who are.
#provide first 5 chars of hashed password
#haveibeenpwned  the website that uses the pwnedpasswords api
#https://passwordsgenerator.net/sha1-hash-generator/



def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res
    


def pwned_api_check(password):
    #check password if it exists in api response
    #print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5],sha1password[5:]
    response = request_api_data(first5_char)
    #print(first5_char,' ',tail)
    
    #return read_res(response)
    return get_password_leaks_count(response,tail)
    
    
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
        #print(h,count)

def  read_res(response):
    print(response.text)
    
#pwned_api_check('123')

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times ... you should probably change your password')
        else:
            print(f'{password} was not found')
    return 'done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
    
  

