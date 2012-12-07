#!/bin/bash
kelias=/home/gymka/Dev/conky_RSS
wget -q -O $kelias/rss1.txt 'http://www.delfi.lt/rss/feeds/daily.xml' 
grep title $kelias/rss1.txt | sed -n 's/.*<title><!\[CDATA\[\(.*\)\]\]><\/title>.*/\1/p'|sed 1,2d|sed -n '1,24p'
rm $kelias/rss1.txt
