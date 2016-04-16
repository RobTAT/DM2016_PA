__author__ = 'yuafan'


from os import listdir
from os.path import isfile, join

try:
    import time
    from lxml import etree
    print "etree success"
    from lxml import objectify
    print "objectify success"
except:
    print "Fail"



mypath = '/.../sample-data/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


tcx_files = []

for fileNames in onlyfiles:

    if '.tcx' in fileNames:
    #if fileNames.find(".tcx"):

        print(fileNames)
        print(mypath + fileNames)

        tcx_files.append(fileNames)

        #tcx = tcxparser.TCXParser(mypath + fileNames)

        #tree = objectify.parse(mypath + fileNames)
        tree = etree.parse(mypath + fileNames)

        #aa = etree.tostring(tree)
        print etree.tostring(tree, pretty_print = True)
