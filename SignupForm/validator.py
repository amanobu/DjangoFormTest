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
    
