#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    Last_digit = number % 0
elif number < 0:
    Last_digit = (abs(number) % 10) * -1)

print("Last-digit of {0} is {1}".format(number, Last_digit), end=" "))
if Last_digit > 5:
    print("and is greater than 5")
elif Last_digit == 0:
    print("and is 0")
elif Last_digit < 6 and Last_digit != 0:
    print("and is less than 6 and not 0")
    
