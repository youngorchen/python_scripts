# encoding: utf-8
#from django import forms
import re,os,sys

__author__ = 'william'

# src=".*? data-original=
# src
#    result, number = re.subn(regex, newstring, subject)

def read_an(an,bn):
    s = set()
    try:
        file = os.path.join("C:/Users/williamchen",an)
        file_object = open(file, encoding="utf-8")
        file_context = file_object.read()
        pat = 'src=".*? data-original='
        result,number = re.subn(pat,"src",file_context, re.M)

        print(result)
        print(number)

        fo = open(bn, "w", encoding="utf-8")
        fo.write(result)


    finally:
        file_object.close()
        fo.close()

#read_an("b100589.html")

for name in os.listdir("C:/Users/williamchen"):
    if os.path.isfile("C:/Users/williamchen/"+name):
        if re.match("b\d+.html",name):
            print(name)
            read_an(name,"p_"+name)
