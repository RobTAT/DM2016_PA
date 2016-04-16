# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
from pprint import pprint
#config=json.loads(open('1652746_24_24_1015660_M_1989_2015_7_180.fit.json').read())
with open('D:/Data Mining/1652746_24_24_1015660_M_1989_2015_7_180.fit.json') as data_file:
    data=json.load(data_file)

def time_convert(time):
    return int(time[11:13]) * 60 * 60 + int(time[14:16]) * 60 + int(time[17:19])


def speed_mean(time, dis):
    return float(dis)/time

timelist = []
dislist = []
#pprint(data)
#data["records"][0]["timestamp"]
for i in range(len(data['records'])):
    #print data['records'][i]['timestamp']
    if 'distance' in data['records'][i]:
        timelist.append(time_convert(data['records'][i]['timestamp']))
        dislist.append(data['records'][i]['distance']);

timelasting = timelist[-1] - timelist[0]
meanSpeed = speed_mean(timelasting, dislist[-1] - dislist[0])
print meanSpeed

'''
count = 0
for i in range(len(timelist) - 1):
    count += 1
    if timelist[i + 1] - timelist[i] < 0:
        break
'''
#print count, timelist[count - 1], timelist[count]

