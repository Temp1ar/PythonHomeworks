#!/bin/env python
import sys

S = str(raw_input())
List = S.split(" ")
if len(List) > 1:
	A = int(List[0])
	B = int(List[1])
	N = int(List[2])
else:
	A = int(S);
	B = int(input());
	N = int(input());

if N > max(B, A):
	print "Impossible"
	sys.exit(0)

if N == A:
	print ">A"
	sys.exit(0)
	
if N == B:
	print ">B"
	sys.exit(0)
	

D = {'A': 0, 'B': 0}
answer = ""
while (N != D['A'] and N != D['B']) and not (D['A'] == 0 and D['B'] == B):
	if (D['A'] == 0):
		D['A'] = A
		answer += ">A\n"
	
	if (D['B'] == B):
		D['B'] = 0
		answer += "B>\n"
	
	howMuch = D['A'] if (D['B'] + D['A']) <= B else (B - D['B'])
	D['B'] = D['B'] + howMuch
	D['A'] = D['A'] - howMuch
	answer += "A>B\n"
	
if (N == D['A'] or N == D['B']):
	print answer
else:
	print "Impossible"
	