# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
from pprint import pprint
#config=json.loads(open('1652746_24_24_1015660_M_1989_2015_7_180.fit.json').read())
with open('1652746_24_24_1015660_M_1989_2015_7_180.fit.json') as data_file:
    data=json.load(data_file)
 
timelist=[]   
#pprint(data)
#data["records"][0]["timestamp"]
for i in data['records']:
    print i['timestamp']
    timelist.append(i['timestamp'])

end_time=timelist[-1]
start_time=data["sessions"][0]["start_time"]
print('end time:',end_time)
print('start time:',start_time)

