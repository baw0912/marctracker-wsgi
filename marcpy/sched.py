#! /usr/bin/env python
import json

sched = []
saSched = []
suSched = []

# NORTHBOUND
tr = { 'Direction' : 'NB', 'Number' : 400, 'Washington' : '5:50', 'Odenton' : '6:19'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 502, 'Washington' : '6:15', 'Odenton' : '6:42'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 404, 'Washington' : '6:35', 'Odenton' : '7:00'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 406, 'Washington' : '7:10', 'Odenton' : '7:38'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 610, 'Washington' : '7:50', 'Odenton' : '8:21'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 612, 'Washington' : '8:20', 'Odenton' : '8:47'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 412, 'Washington' : '9:05', 'Odenton' : '9:33'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 414, 'Washington' : '9:30', 'Odenton' : '9:57'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 416, 'Washington' : '10:30', 'Odenton' : '10:57'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 418, 'Washington' : '11:20', 'Odenton' : '11:47'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 520, 'Washington' : '12:20 PM', 'Odenton' : '12:47 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 422, 'Washington' : '1:20 PM', 'Odenton' : '1:47 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 424, 'Washington' : '2:20 PM', 'Odenton' : '2:47 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 426, 'Washington' : '3:23 PM', 'Odenton' : '3:51 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 428, 'Washington' : '4:10 PM', 'Odenton' : '4:39 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 532, 'Washington' : '4:25 PM', 'Odenton' : '4:56 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 634, 'Washington' : '4:40 PM', 'Odenton' : '5:09 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 536, 'Washington' : '5:10 PM', 'Odenton' : '5:35 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 440, 'Washington' : '5:25 PM', 'Odenton' : '5:56 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 642, 'Washington' : '5:50 PM', 'Odenton' : '6:18 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 544, 'Washington' : '6:23 PM', 'Odenton' : '6:51 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 446, 'Washington' : '6:40 PM', 'Odenton' : '7:09 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 448, 'Washington' : '7:40 PM', 'Odenton' : '8:08 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 548, 'Washington' : '9:00 PM', 'Odenton' : '9:28 PM'}
sched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 452, 'Washington' : '10:30 PM', 'Odenton' : '10:57 PM'}
sched.append(tr)

# SOUTHBOUND
tr = { 'Direction' : 'SB', 'Number' : 401, 'Odenton' : '4:49', 'Washington' : '5:24'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 403, 'Odenton' : '5:24', 'Washington' : '5:56'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 505, 'Odenton' : '5:49', 'Washington' : '6:21'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 407, 'Odenton' : '6:17', 'Washington' : '6:50'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 409, 'Odenton' : '6:39', 'Washington' : '7:07'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 511, 'Odenton' : '6:52', 'Washington' : '7:25'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 413, 'Odenton' : '7:12', 'Washington' : '7:44'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 415, 'Odenton' : '7:26', 'Washington' : '7:59'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 517, 'Odenton' : '7:41', 'Washington' : '8:06'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 419, 'Odenton' : '8:04', 'Washington' : '8:36'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 421, 'Odenton' : '8:34', 'Washington' : '9:07'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 523, 'Odenton' : '9:29', 'Washington' : '10:04'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 425, 'Odenton' : '9:49', 'Washington' : '10:20'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 427, 'Odenton' : '10:47', 'Washington' : '11:19'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 429, 'Odenton' : '11:57', 'Washington' : '12:29'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 431, 'Odenton' : '12:57 PM', 'Washington' : '1:29 PM'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 433, 'Odenton' : '1:57 PM', 'Washington' : '2:29 PM'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 435, 'Odenton' : '2:57 PM', 'Washington' : '3:29 PM'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 439, 'Odenton' : '4:07 PM', 'Washington' : '4:39 PM'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 641, 'Odenton' : '4:39 PM', 'Washington' : '5:08 PM'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 443, 'Odenton' : '5:08 PM', 'Washington' : '5:40 PM'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 445, 'Odenton' : '5:48 PM', 'Washington' : '6:20 PM'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 449, 'Odenton' : '6:45 PM', 'Washington' : '7:15 PM'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 451, 'Odenton' : '7:56 PM', 'Washington' : '8:27 PM'}
sched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 453, 'Odenton' : '9:41 PM', 'Washington' : '10:15 PM'}
sched.append(tr)

# SATURDAY - NORTHBOUND
tr = { 'Direction' : 'NB', 'Number' : 476, 'Washington' : '9:02', 'Odenton' : '9:26'}
saSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 478, 'Washington' : '10:02', 'Odenton' : '10:26'}
saSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 482, 'Washington' : '12:30 PM', 'Odenton' : '12:54 PM'}
saSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 688, 'Washington' : '4:10 PM', 'Odenton' : '4:34 PM'}
saSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 490, 'Washington' : '4:50 PM', 'Odenton' : '5:14 PM'}
saSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 492, 'Washington' : '5:30 PM', 'Odenton' : '5:54 PM'}
saSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 494, 'Washington' : '7:50 PM', 'Odenton' : '8:14 PM'}
saSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 696, 'Washington' : '9:30 PM', 'Odenton' : '9:54 PM'}
saSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 698, 'Washington' : '10:35 PM', 'Odenton' : '10:59 PM'}
saSched.append(tr)


# SATURDAY - SOUTHBOUND
tr = { 'Direction' : 'SB', 'Number' : 675, 'Odenton' : '7:59', 'Washington' : '8:35'}
saSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 677, 'Odenton' : '8:54', 'Washington' : '9:30'}
saSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 481, 'Odenton' : '11:29', 'Washington' : '12:05 PM'}
saSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 487, 'Odenton' : '2:44 PM', 'Washington' : '3:20 PM'}
saSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 689, 'Odenton' : '3:34 PM', 'Washington' : '4:10 PM'}
saSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 491, 'Odenton' : '4:34 PM', 'Washington' : '5:10 PM'}
saSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 495, 'Odenton' : '6:49 PM', 'Washington' : '7:25 PM'}
saSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 497, 'Odenton' : '8:14 PM', 'Washington' : '8:50 PM'}
saSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 499, 'Odenton' : '9:39 PM', 'Washington' : '10:15 PM'}
saSched.append(tr)

# SUNDAY - NORTHBOUND
tr = { 'Direction' : 'NB', 'Number' : 480, 'Washington' : '10:45', 'Odenton' : '11:09'}
suSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 484, 'Washington' : '12:45 PM', 'Odenton' : '1:09 PM'}
suSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 486, 'Washington' : '2:30 PM', 'Odenton' : '2:54 PM'}
suSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 488, 'Washington' : '3:45 PM', 'Odenton' : '4:09 PM'}
suSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 692, 'Washington' : '5:30 PM', 'Odenton' : '5:54 PM'}
suSched.append(tr)
tr = { 'Direction' : 'NB', 'Number' : 694, 'Washington' : '7:00 PM', 'Odenton' : '7:24 PM'}
suSched.append(tr)

# SUNDAY - SOUTHBOUND
tr = { 'Direction' : 'SB', 'Number' : 681, 'Odenton' : '9:39', 'Washington' : '10:15'}
suSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 683, 'Odenton' : '11:29', 'Washington' : '12:05 PM'}
suSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 485, 'Odenton' : '1:14 PM', 'Washington' : '1:50 PM'}
suSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 487, 'Odenton' : '2:44 PM', 'Washington' : '3:20 PM'}
suSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 491, 'Odenton' : '4:34 PM', 'Washington' : '5:10 PM'}
suSched.append(tr)
tr = { 'Direction' : 'SB', 'Number' : 493, 'Odenton' : '5:54 PM', 'Washington' : '6:30 PM'}
suSched.append(tr)




def getOdentonTime(number):
	for tr in sched:
		if tr['Number'] == number :
			return tr['Odenton']
	for tr in saSched:
		if tr['Number'] == number :
			return tr['Odenton']
        for tr in suSched:
                if tr['Number'] == number :
                        return tr['Odenton']


def getWashingtonTime(number):
	for tr in sched:
		if tr['Number'] == number :
			return tr['Washington']
	for tr in saSched:
		if tr['Number'] == number :
			return tr['Washington']
        for tr in suSched:
                if tr['Number'] == number :
                        return tr['Washington']

