#!/bin/env python
from collections import defaultdict

# From here http://www.delinguis.com/art/levenstein
def distance(source, dest):
    '''
    Count Levenstein distanse for source and destination sequences.
    '''
    if source == dest:
        return 0

    # Prepare matrix
    slen, dlen = len(source), len(dest)
    dist = [[0 for i in range(dlen+1)] for x in range(slen+1)]
    for i in xrange(slen+1):
        dist[i][0] = i
    for j in xrange(dlen+1):
        dist[0][j] = j

    # Counting distance
    for i in xrange(slen):
        for j in xrange(dlen):
            cost = 0 if source[i] == dest[j] else 1
            dist[i+1][j+1] = min(
                            dist[i][j+1] + 1,   # deletion
                            dist[i+1][j] + 1,   # insertion
                            dist[i][j] + cost   # substitution
                        )
    return dist[-1][-1]
    	
input = open("games.txt")
lines = input.read().split("\n");

root = lines[0].strip()
target = lines[1].strip()
size = int(lines[2].strip())

words = []
for i in range(3, 3+size):
	words.append(lines[i].strip());
words.append(target);
	

queue = [(root, 0)]
chain = [];

combobreaker = False
while (len(queue) > 0):
	v = queue.pop()
	chain.append(v);
	for word in [word for word in words if distance(v[0], word) == 1]:
		words.remove(word)
		queue.append((word, v[0]))
		if(word == target):
			combobreaker = True
			break
	if (combobreaker):
		break

if distance(chain[-1][0], target) == 1:
	last = (chain[-1][0], chain[-1][1])
	answer = []
	
	dict = {}
	for v, k in chain:
		dict[v] = k
	
	while (last[1] != 0):
		answer.insert(0, last[0])
		last = (last[1], dict[last[1]])
	answer.insert(0, root);
	answer.append(target);

	print "\n".join(answer)
else:
	print "Impossible"