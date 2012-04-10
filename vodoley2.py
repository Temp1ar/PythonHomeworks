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

if (N % A == 0):
	print ">A\nA>C\n" * int(N / A);
	sys.exit(0)
	
if (N % B == 0):
	print ">B\nB>C\n" * int(N / B);
	sys.exit(0)

D = {'A': 0, 'B': 0}

maxdivisor = divisor = 0
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
	if (N % (D['A'] + D['B']) == 0):
		divisor = D['A'] + D['B']
		if (maxdivisor == 0 or divisor > maxdivisor):
			bestanswer = answer
			maxdivisor = divisor		
	
if maxdivisor == 0:
	print "Impossible"
else:
	print (bestanswer + "A>C\nB>C\n") * int(N / maxdivisor)
	