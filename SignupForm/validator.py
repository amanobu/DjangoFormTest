# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re

def validate_number(value):
    print("method validate_number")
    return value.isdigit()

def validate_zip1(value):
    print("method validate_zip1")
    if validate_number(value):
        num = int(value)
        print("zip1:"+str(num))
        if 100 <= num and num < 1000:
            print("zip1 OK:"+str(num))
            return True
    print("zip1 NG")
    return False
            

def validate_zip2(value):
    print("method validate_zip2")
    if validate_number(value):
        num = int(value)
        print("zip2:"+str(num))
        if 0 <= num and num < 10000:
            print("zip2 OK:"+str(num))
            return True
    print("zip2 NG")
    return False

def validate_name(fname,lname):
    if fname and lname:
        name = fname + lname
        name_length = len(name)
        print(name)
        print(name_length)
        if 2 <= name_length and name_length <= 8:
            return True
    return False

def validate_userid(userid):
    #TODO:あとで文字列を制限するコードを記載
    return True
