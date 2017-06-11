#!/usr/env python
# -*_ coding:UTF-8 -*-
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

__author__ = 'neo'

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())
print(bsObj)