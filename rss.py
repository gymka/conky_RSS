#!/usr/bin/python2
# coding: utf-8
import feedparser
import sys
#sys.setdefaultencoding('utf-8')

def gaut_rss(kuris, kiek):
	#delfi lietuvoje http://www.delfi.lt/rss/feeds/lithuania.xml
	#delfi uzsienyje http://www.delfi.lt/rss/feeds/world.xml
	rss=feedparser.parse(kuris)
	i=0
	while i<kiek:
		print(rss.entries[i]['title']).encode('utf-8')
		i+=1
	print("%s" % ("-"*80)).encode('utf-8')
try:
	gaut_rss(sys.argv[1],int(sys.argv[2]))
except:
	#	print("Naudojimas: ./rss.py rss_srautas naujienu_skaicius\nPvz.
	gaut_rss("http://www.delfi.lt/rss/feeds/lithuania.xml",8)
	gaut_rss("http://www.delfi.lt/rss/feeds/world.xml",8)
	gaut_rss("http://www.linkomanija.net/rss.php?feed=dl&cat[]=51&cat[]=64&cat[]=65&passkey=e588d60fe1d51bf2f372550e1f51008b",8)
