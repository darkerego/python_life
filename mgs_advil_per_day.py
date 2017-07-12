#!/usr/bin/python

""" Calculates how many milligrams of 
advil per day one may need each morning. """
import sys

advil_per_day = ''
age=0

try:
    age=sys.argv[1]
    age=int(age)
except IndexError:
    age=''
    try:
        age = raw_input("How many years you got : ")
        age=int(age)
    except:
        pass
    pass

def fml(age):

    advil_per_day = 0
    int(advil_per_day)
    int(advil_per_day) == '0'

    advil_per_day = age * (age % 222)
    return int(advil_per_day)

advil_per_day = fml(age)
print advil_per_day
