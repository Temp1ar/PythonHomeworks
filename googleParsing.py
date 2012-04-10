#!/bin/env python
# coding: UTF-8
import urllib
import re

class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1" +
			  "(KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1"
urllib._urlopener = AppURLopener()

query = "бляхамуха"
query = "some nice python tricks cool"
params = urllib.urlencode({'q': query, 'ie': "UTF-8"})
google_results = urllib.urlopen("http://www.google.com/search?%s" % params)

results = []
for item in google_results.read().split("</cite>"):
	if "<cite>" in item:
		address = item [ item.find("<cite>")+len("<cite>") : ]
		domain = re.search(r'\.([a-z]*)\/', address)
		if domain: 
			results.append( domain.group(1) )


answer = {}
[answer.__setitem__(item,1+answer.get(item,0)) for item in results]
print answer
			
