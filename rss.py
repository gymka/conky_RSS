#!/usr/bin/python
import feedparser
import sys

def gaut_rss(kuris, kiek):
	#delfi lietuvoje http://www.delfi.lt/rss/feeds/lithuania.xml
	#delfi užsienyje http://www.delfi.lt/rss/feeds/world.xml
	rss=feedparser.parse(kuris)
	i=0
	while i<kiek:
		print(rss.entries[i]['title'])
		i+=1
	print("---------------------------------------------------")
try:
	gaut_rss(sys.argv[1],int(sys.argv[2]))
except:
	print("Naudojimas: ./rss.py rss_srautas naujienų_skaičius\nPvz. ./rss.py \"http://www.delfi.lt/rss/feeds/lithuania.xml\" 10")
