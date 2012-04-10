#!/bin/env python
import sys

first = raw_input()
first = first.split(" ")
n = int(first[0]);
m = int(first[1]);

persons = {}
marks = {}
for i in range(m):
	line = raw_input()
	line = line.split(" ")
	f = int(line[0])
	s = int(line[1])
	if persons.has_key(f):
		persons[f].append(s)
	else:
		persons[f] = [s]
	if persons.has_key(s):
		persons[s].append(f)
	else:
		persons[s] = [f]

marks = dict.fromkeys(persons.keys())		

def dfs(graph, start, color, path=[]):
	path = path + [start]
	if graph.has_key(start):		
		for node in graph[start]:
			if not node in path:
				marks[node] = color
				path = dfs(graph, node, not color, path)
			else:
				if marks[node] != color:
					print "NO"
					sys.exit()
	return path
	
while (None in marks.values()):
	for k in marks.keys():
		if(marks[k] == None):
			i = k
			break
	marks[i] = False
	dfs(persons, i, True)

print "YES"
for k in marks.keys():
	if(marks[k]):
		print k,