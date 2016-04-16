def time_convert(time):
    return int(time[11:13]) * 60 * 60 + int(time[14:16]) * 60 + int(time[17:19])


def speed_mean(time, dis):
    return float(dis)/time

def get_meanSpeed(data):
    timelist = []
    dislist = []
    #pprint(data)
    #data["records"][0]["timestamp"]
    if 'records' in data:
        for i in range(len(data['records'])):
            #print data['records'][i]['timestamp']
            if 'distance' in data['records'][i]:
                timelist.append(time_convert(data['records'][i]['timestamp']))
                dislist.append(data['records'][i]['distance']);
    if len(timelist) != 0:
        timelasting = timelist[-1] - timelist[0]
        meanSpeed = speed_mean(timelasting, dislist[-1] - dislist[0])
        return meanSpeed
    else:
        return 0