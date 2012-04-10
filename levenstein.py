#!/bin/env python

def distance(source, dest):
    if source == dest:
        return 0

    slen, dlen = len(source), len(dest)
    dist = [[0 for i in range(dlen+1)] for x in range(slen+1)]
    for i in xrange(slen+1):
        dist[i][0] = i
    for j in xrange(dlen+1):
        dist[0][j] = j

    for i in xrange(slen):
        for j in xrange(dlen):
            cost = 0 if source[i] == dest[j] else 1
            dist[i+1][j+1] = min(
                            dist[i][j+1] + 1,  
                            dist[i+1][j] + 1,   
                            dist[i][j] + cost 
                        )
    return dist[-1][-1]

fromString = raw_input()
toString = raw_input()

print distance(fromString, toString)
