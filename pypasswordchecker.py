#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 04:34:16 2020

@author: tech

checks is password has ever been hacked

"""
import requests

#kind of like having a browser w/o having a browser
#the api uses hashed passwords not plain text (sha1)
#The api uses k anonymity allows someone to receive info about us w/o them knowing
#who are.
#provide first 5 chars of hashed password
#haveibeenpwned  the website that uses the pwnedpasswords api
#https://passwordsgenerator.net/sha1-hash-generator/

url = 'https://api.pwnedpasswords.com/range/'+ 'CBFDA'
res = requests.get(url)
print(res)
