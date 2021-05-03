#!/bin/python

print("Another demo - from 02_open_file.py")

with open('resources/02_file.txt') as f:
    print(f.readlines())
