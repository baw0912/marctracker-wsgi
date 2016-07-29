#! /usr/bin/env python
import json
from time import localtime, strftime
from sched import sched, saSched, suSched
from templates import south_t, north_t, index_t

def makeSouthTrainText(train):
	return makeSubs(south_t, train)

def makeNorthTrainText(train):
	return makeSubs(north_t, train)

def makeSubs(t, train):
	t=t.replace('${Number}',train['Number'])
	t=t.replace('${OdentonTime}',train['OdentonTime'])
	t=t.replace('${WashingtonTime}',train['WashingtonTime'])
	t=t.replace('${NextStation}',train['NextStation'])
	t=t.replace('${Status}',train['Status'])
	t=t.replace('${Delay}',train['Delay'])
	t=t.replace('${EstDepart}',train['EstDepart'])
	t=t.replace('${LastUpdated}',train['LastUpdated'])
	return t
	
def addStatus(trains, outText):
	tmpText = outText
	trainText = ""
	for train in trains['PENN SOUTH']:
		try:
			trainText += makeSouthTrainText(train)
		except:
			pass
	
	tmpText = tmpText.replace('${SOUTH}', trainText)

	trainText = ""
	for train in trains['PENN NORTH']:
		try:
			trainText += makeNorthTrainText(train)
		except:
			pass

	tmpText = tmpText.replace('${NORTH}', trainText)
	tmpText = tmpText.replace('${TIME}', strftime("%I:%M %p %a %m/%d", localtime()))

	return tmpText

def addSchedule(outText):
	northText = ''
	southText = ''
	tmpText = outText

	for train in sched:
		if train['Direction'] == 'NB':
			tmpStr = '<tr><td>'+str(train['Number'])+'</td><td>'+train['Washington']+'</td><td>'+train['Odenton']+'</tr>\n'
			northText += tmpStr
		elif train['Direction'] == 'SB':
			tmpStr = '<tr><td>'+str(train['Number'])+'</td><td>'+train['Odenton']+'</td><td>'+train['Washington']+'</tr>\n'
			southText += tmpStr

	tmpText = tmpText.replace('${NORTH_SCHEDULE}', northText)
	tmpText = tmpText.replace('${SOUTH_SCHEDULE}', southText)

	northText = ''
	southText = ''

	for train in suSched:
		if train['Direction'] == 'NB':
			tmpStr = '<tr><td>'+str(train['Number'])+'</td><td>'+train['Washington']+'</td><td>'+train['Odenton']+'</tr>\n'
			northText += tmpStr
		elif train['Direction'] == 'SB':
			tmpStr = '<tr><td>'+str(train['Number'])+'</td><td>'+train['Odenton']+'</td><td>'+train['Washington']+'</tr>\n'
			southText += tmpStr

	tmpText = tmpText.replace('${NORTH_SU_SCHEDULE}', northText)
	tmpText = tmpText.replace('${SOUTH_SU_SCHEDULE}', southText)

	northText = ''
	southText = ''

	for train in saSched:
		if train['Direction'] == 'NB':
			tmpStr = '<tr><td>'+str(train['Number'])+'</td><td>'+train['Washington']+'</td><td>'+train['Odenton']+'</tr>\n'
			northText += tmpStr
		elif train['Direction'] == 'SB':
			tmpStr = '<tr><td>'+str(train['Number'])+'</td><td>'+train['Odenton']+'</td><td>'+train['Washington']+'</tr>\n'
			southText += tmpStr

	tmpText = tmpText.replace('${NORTH_SA_SCHEDULE}', northText)
	tmpText = tmpText.replace('${SOUTH_SA_SCHEDULE}', southText)
	return tmpText

def buildHTML(trains):
	outText = index_t
	outText = addStatus(trains, outText)
	outText = addSchedule(outText)
	return outText

if __name__ == "__main__":
	trains = json.loads(open('out.json').read())
	text = buildHTML(trains)
	open('index.html', 'w').write(text)
