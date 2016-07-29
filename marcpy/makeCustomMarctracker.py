#! /usr/bin/env python

import get, parse, build
import os

outFilename = 'index.html'
outDestination = '/var/www/mt'

def getHTML():
	htmlIn = get.getMarctrackerHTML()
	#htmlIn = open('mt.html').read()
	trains = parse.parseMarctrackerHTML(htmlIn)
	htmlOut = build.buildHTML(trains)
	return htmlOut

def writeHere():
	htmlOut = getHTML()
	f = open(outFilename, 'w')
	f.write(htmlOut)
	f.close()

if __name__ == '__main__':
	htmlOut = getHTML()
	open(outFilename, 'w').write(htmlOut)
	#os.rename(outFilename, outDestination + '/' + outFilename)
