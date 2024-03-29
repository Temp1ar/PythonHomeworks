import sys
from itertools import *

def powerset(iterable, count):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) 
        for r in range(1, min(len(s) + 1, count + 1)))

def take(n, iterable):
    answer = set()
    for x in iterable:
        if len(answer) < n:
            answer.add(''.join(x))
        else:
            break
    return answer

def try_kuhn(v, used, mt, edges, rightPartie):
    if used[v]:
        return False
    used[v] = True
    for i in xrange(len(edges[v])):
        toWord = edges[v][i]
        to = rightPartie.index(toWord)
        if mt[to] == -1 or try_kuhn(mt[to], used, mt, edges, rightPartie):
            mt[to] = v
            return True
    return False

input = open("input.txt")
words = input.read().split()[1:]
input.close()

leftPartie = words
rightPartie = set()
edges = []
for word in words:
    shortages = take(len(words), powerset(word, 4))
    edges.append(list(shortages))
    rightPartie.update(shortages)

rightPartie = list(rightPartie)

k = len(rightPartie)
mt = [-1] * k
n = len(leftPartie)
for v in xrange(n):
    used = [False] * n
    try_kuhn(v, used, mt, edges, rightPartie)

out = open("output.txt", 'w')
if max(mt) < len(words) - 1:
    out.write("-1")
    out.close()
    print "-1"
    sys.exit(0)

for i in xrange(n):
    ind = mt.index(i)
    print words[i], rightPartie[ind]
    out.write(rightPartie[ind] + "\n")
    
out.close()
sys.exit(0)