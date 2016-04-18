import json
import os
import glob
import prepocessing_Json as Pre

from pprint import pprint

path = 'D:/Data Mining/Json'
#config=json.loads(open('1652746_24_24_1015660_M_1989_2015_7_180.fit.json').read())

data=[]
for filename in glob.glob(os.path.join(path, '*.json')):
    with open(filename) as data_file:
        data.append(json.load(data_file))

for i in range(len(data)):
    print Pre.get_meanSpeed(data[i])

for i in range(len(data)):
    print Pre.get_maxSpeed(data[i])