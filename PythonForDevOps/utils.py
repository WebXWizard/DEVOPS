# Libraries in Python

import os # Importing the os module to interact with the operating system

print("Current Working Directory: ", os.getcwd())
print(os.system("ls -l"))
print(os.system("systeminfo"))
print(os.system("pwd"))
print(os.system("df -h"))
print(os.system("whoami"))
print(os.system("date"))

import math # Importing the math module for mathematical functions

print("Value of Pi: ", math.pi)
print("Square root of 16: ", math.sqrt(16))
print("Factorial of 5: ", math.factorial(5))

import random # Importing the random module for generating random numbers

print("Random number between 1 and 10: ", random.randint(1, 10))
print("Random choice from a list: ", random.choice(['apple', 'banana', 'cherry']))
print("Random float between 0 and 1: ", random.random())

import datetime # Importing the datetime module for date and time operations

now = datetime.datetime.now()
print("Current Date and Time: ", now)
print("Current Year: ", now.year)
print("Current Month: ", now.month)
print("Current Day: ", now.day)

import json # Importing the json module for JSON operations

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data)
print("JSON Data: ", json_data)
parsed_data = json.loads(json_data)
print("Parsed Data: ", parsed_data)

import re # Importing the re module for regular expressions

pattern = r'\bfoo\b'
text = 'foo bar baz foo'
matches = re.findall(pattern, text)
print("Matches for 'foo': ", matches)


import sys # Importing the sys module for system-specific parameters and functions

print("Python Version: ", sys.version)
print("Platform: ", sys.platform)
print("Script Name: ", sys.argv[0])
print("Module Search Path: ", sys.path)


