import os
import json
import sys
import threading
from threading import *
import time

def create(key, value, fpath, timeout=0):
    # value = str(value)
    size = os.path.getsize(fpath)/(1024*1024)
    if size <= 1023: # If size of the file is less than 1GB
        with open(fpath, 'r') as json_file:
            data = json.load(json_file)
        if key in data: 
            print("Error: This key already exists")
        elif len(key) > 32: # Checking for the length of the key
            print("Error: Key length exceeded")
        elif all(x.isalpha() or x.isspace() for x in key) == False: # Ensuring our key only has alphabets and spaces only
            print('Error: Key should contain only alphabets')
        elif sys.getsizeof(value) > 16000: # Checking the size of the value
            print('Error: The size of value should not exceed 16 KB')
            return
        else:
            if timeout > 0:
                value = [value, time.time()+timeout]
            else:
                value = [value, timeout]
            data[key] = value
            json.dump(data, open(fpath,'w'), indent=2)
            print('Key created successfully')
    else:
        print("File size exceeded")

def read(key, fpath):
    with open(fpath, 'r') as json_file:
        data = json.load(json_file)
    if  key not in data:
        print('Error: The key does not exists in database')
    else:
        temp = data[key]
        if temp[1] != 0:# If the timeout is not 0 it checks for the expiry
            if time.time() < temp[1]: # Checking the expiry of the key
                print(str(key)+':'+str(temp[0]))
                return
            else:
                print('Error:', key, 'has expired')
        else:
            print(str(key)+':'+str(temp[0])) # Printing the key and value in JSON format
    pass

def delete(key, fpath):
    with open(fpath, 'r') as json_file:
        data = json.load(json_file)
    if key not in data:
        print('Error: The key does not exists in database')
    else:
        temp = data[key]
        if temp[1] != 0:# If the timeout is not 0 it checks for the expiry
            if time.time() < temp[1]: # Checking the expiry of the key
                del data[key]
                print(key, 'is deleted successfully')
                json.dump(data, open(fpath,'w'), indent=2)
                return
            else:
                print('Error:', key, 'has expired')
        else:
            del data[key]
            print(key, ' is deleted successfully')
            json.dump(data, open(fpath,'w'), indent=2)

def create_file():
    a = int(input('Enter 1 - If you want it at specific location, else - 0'))
    # creating a file at random location
    if a == 0:
        f = open("data.json", "w")
        path = f.name
    # creating a file at specific location
    else:
        fpath  = input('Enter the path')
        file = os.path.join(fpath, "data.json")
        f = open(file, "w")
        path = f.name
    return path

# This code also checks and displays errors like not valid key names.