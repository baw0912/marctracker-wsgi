#! /usr/bin/env python

import httplib

def getMarctrackerHTML():
	conn = httplib.HTTPConnection("www.marctracker.com")
	conn.request("GET", "/PublicView/status.jsp")
	rsp = conn.getresponse();
	return rsp.read()

if __name__ == "__main__":
	print getMarctrackerHTML()
