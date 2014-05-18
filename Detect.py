__author__ = 'Per'
# 12.04.14
# works, working on XML-Parser-Integration minidom

from class_logentry import logentry
from class_cachelogs import cachelogs
from class_cache import cache
import xml.dom.minidom

fo = ""
def findDupes(cachelog):

    x = cachelog.getLogs()
    y = []
    i = []
    gccode = cachelog.cache.gccode
    for f in range(1, len(x) + 1):
        if x[-f].logtype != 'Found it':
            i.append(x[-f])
        else:
            y.append(x[-f])
    f = len(y)
    if f >= 2:

        fo.write(
            "<html>\n <head>\n<title>  GC DupeDetect </title>\n <link href='DupeDetectColors.css' rel='stylesheet'/> \n"
            "</head>\n<body>\n<img src='./img/dupedetect.png' hight='45'/>\n"
            " <h2>\n<a href='http://coords.info/" + gccode + "'target='blank'> Cache " + gccode +
            "</a>\n</h2>")
    else:

        fo.write(
            "<html>\n <head>\n<title>  GC DupeDetect </title>\n  <link href='DupeDetectColors.css' rel='stylesheet'/> \n"
            "</head>\n<body>\n<img src='./img/dupedetect.png' hight='45'/>\n <h3 style='background-color: red; color: "
            "blue'> No dupes detected! </h3>")

    if f >= 2:
        fo.write(" \n <h3 > These are the found-logs:  </h3> \n")
        for log in y:
            x = str(log.printlog())
            y = str(log.logid)
            fo.write(
                " <h4> <a href='http://www.geocaching.com/seek/log.aspx?LID=" + y + "'target='blank'> " + x + " </a> </h4> \n")

    if len(i) >= 1:
        fo.write(" \n  <p>  </p> \n  <p>  </p> \n <h3> These are the other logs: </h3> \n")

    for log in i:
        x = str(log.printlog())
        y = str(log.logid)
        fo.write(
            " <h4> <a href='http://www.geocaching.com/seek/log.aspx?LID=" + y + "'target='_blank'> " + x + " </a> </h4> \n")

    fo.write("\n</body>\n</html>")
    print("\n \n \t \t HTML created. View DupeDetectWeb.hmtl and open in Browser for overview over your results \n \n")







def getTextFromDomElement(domElement, elementName):
    return domElement.getElementsByTagName(elementName)[0].firstChild.wholeText



def readLogs():
    for log in logs:
        logid = log.attributes["id"].value
        logtype = getTextFromDomElement(log, "groundspeak:type")
        logdate = getTextFromDomElement(log, "groundspeak:date")
        logtext = getTextFromDomElement(log, "groundspeak:text")
        le1 = logentry(logid, logtype, logdate, logtext)
        logentries.append(le1)
    return logentries

def printLogs():
    for log in logentries:
       print(log.printlog())

def addLogs():
    for log in logentries:
        log1.add_logentry(log)




all_caches = []
logentries = []



filename = "./pocketqueries/test-cachelist.xml"
dom = xml.dom.minidom.parse(filename)
waypoints = dom.getElementsByTagName('wpt')
fo = open("DupeDetectWeb.html", "w")
i = 1
for wpt in waypoints:
    geocode = getTextFromDomElement(wpt, "name")
    geoname = getTextFromDomElement(wpt,"urlname")
    cache1 = cache(geocode, geoname)
    cachelog = cachelogs(cache1)
    logs = wpt.getElementsByTagName("groundspeak:log")
    for log in logs:
        log_id = log.attributes['id'].value
        log_type = getTextFromDomElement(log, "groundspeak:type")
        log_date = getTextFromDomElement(log, "groundspeak:date")
        log_text = getTextFromDomElement(log, "groundspeak:text")
        log_entry = logentry(log_id, log_type, log_date, log_text)
        cachelog.add_logentry(log_entry)
        print("test")
    all_caches.append(cachelog)
    findDupes(cachelog)
    print(i)
    i += 1



# print(all_caches)
# cache_log = all_caches[0]
# print(cache_log.cache.gccode)
# z = cache_log.getLogs()
