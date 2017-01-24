import sys,json
template='temple.json'
user_default='user_default'
def doCheck():
    try:
        tf=open(template,'r')

        file = sys.argv[1]
        print "# Chek FILE=", file
        f = open(file, 'r')
        dataJson = json.load(f)
    except:
        print "File Open Error!"
        exit(-1)
    templeJson= json.load(tf)
    #print json.dumps(templeJson)
    groupDict = dataJson[user_default]
    print groupDict
    for tkey  in templeJson:
        tval=templeJson[tkey]
        if tval != groupDict.get(tkey):
            print "NG ",tkey,"=",groupDict.get(tkey)

if __name__ == '__main__':
    doCheck()


#for ckKey , ckValue in groupDict.iteritems():

