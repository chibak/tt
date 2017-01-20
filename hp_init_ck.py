import sys,json
template='temple.json'

tf=open(template,'r')
file = sys.argv[1]
print "# Chek FILE=", file
f = open(file, 'r')
dataJson = json.load(f)

templeJson= json.load(tf)

print json.dumps(templeJson)

keyList = dataJson.keys()
keyList.sort()
for key in keyList:
    if key != "user_default":
        continue
    else:
        groupDict = dataJson[key]
        print groupDict
        for tkey  in templeJson:
            tval=templeJson[tkey]
            if tval != groupDict.get(tkey):
                print "NG ",tkey,"=",groupDict.get(tkey)


        '''
       '''



#for ckKey , ckValue in groupDict.iteritems():

