# encoding: utf-8
#from django import forms
#import re

__author__ = 'william'

import os,re

#/Dashboard/Editor/103098?guid=8774bda68afded6cc1b89bc29c21d8cf


def read_an(an):
    s = set()
    try:
        file = os.path.join("C:/Users/williamchen",an)
        file_object = open(file,encoding="utf-8")
        file_context = file_object.read()
        pat = "Dashboard/Editor/(\d+)\?guid=8774bda68afded6cc1b89bc29c21d8cf"
        result = re.findall(pat,file_context, re.M)

        #print(result)
        for i in result:
            s.add(i)
        return s
    finally:
        file_object.close()

for i in range(44):
    result = read_an("a{0}.html".format(str(i)))
    #print(result)
    for k in result:
        print("curl --retry 10 --retry-delay 100  --retry-max-time 100 http://nzago.kiwifield.com/Home/Detail/{0} > b{0}.html".format(k))