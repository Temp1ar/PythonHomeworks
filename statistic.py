#!/bin/env python

file = open("statist.txt");
lines = file.read().split("\n");
print lines;

for line in lines:
    dict = {}
    for char in line:
        if(char == ' '):
            continue
        if(char not in dict):
            dict[char] = 1
        else:
            dict[char] = dict[char] + 1;
    s = ""
    for key, value in sorted(dict.iteritems(), key=lambda (k,v): (v,k)):
        s = str(key) + str(value) + " " + s
    print s

