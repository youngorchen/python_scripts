# encoding: utf-8
#from django import forms
import re

__author__ = 'william'

"""Module documentation goes here
"""

path = './'

s = set()

with open(path + 'mail', 'r', encoding='utf-8') as f1:
    lines = f1.readlines()
    for line in lines:
        for item in line.replace(" ",';').replace(",",';').replace("\n",'').split(';'):
            if item.find('@') == -1:
                continue
            print(item)
            s.add(item)

#s = sorted(list(s), key=lambda i : len(i))
s = sorted(list(s), key=lambda i : i[0])
#list(s).sort()
#s = set(s)
with open(path + 'mail.txt', 'w', encoding='utf-8') as fout:
    for i in s:
        fout.writelines(i + '\n')


