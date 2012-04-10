#!/bin/env python

# big greek letters
for i in range(ord(u'\u0391'), ord(u'\u03A9')):
	print unichr(i),

print ""
	
# small greek letters
for i in range(ord(u'\u03B1'), ord(u'\u03C9')):
	print unichr(i),