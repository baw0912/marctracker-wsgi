#! /usr/bin/env python

from bs4 import BeautifulSoup
import json
import sched

def parseMarctrackerHTML(htmlText):
	soup = BeautifulSoup(htmlText)
	lines = soup.find_all("td", "textStatusLine")

	lines_d = {}

	for line in lines:
		if not line.text.strip().startswith('PENN'):
			continue
		line_d = []
		trains = line.parent.parent.find_all("tr", "textStatusAll")
		for train in trains:
			atts = train.find_all("td")

			train_d = {}
			train_d['Number'] = atts[2].text.strip()
			train_d['NextStation'] = atts[3].text.strip()
			train_d['EstDepart'] = atts[4].text.strip()
			train_d['Status'] = atts[5].text.strip()
			train_d['Delay'] = atts[6].text.strip()
			train_d['LastUpdated'] = atts[7].text.strip()
			train_d['OdentonTime'] = sched.getOdentonTime(int(train_d['Number']))
			train_d['WashingtonTime'] = sched.getWashingtonTime(int(train_d['Number']))
			line_d.append(train_d)
	
		lines_d[line.text.strip()] = line_d

	return lines_d

if __name__ == "__main__":
	lines_d = parseMarctrackerHTML(open('mt.html').read())
	print json.dumps(lines_d, sort_keys=True, indent=3)
