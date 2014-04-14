# example xml reader for gpx files
import xml.dom.minidom

# from xml.dom.minidom import Node

filename = 'test-cachelist.xml'

def printFileStatistics( dom, waypoints ):
	nrOfLogs = dom.getElementsByTagName('groundspeak:log').length
	nrOfCaches = dom.getElementsByTagName('groundspeak:cache').length
	print "\n"*3
	print "File Statistics:"
	print 'file %s contains %d waypoints, %d caches and %d logs.' % (filename, waypoints.length, nrOfCaches, nrOfLogs)
	print '='*70, "\n"



def printWayPoint( wpt, nrOfLogs ):
	wname     = getTextFromDomElement( wpt, 'name')
	cacheName = getTextFromDomElement( wpt, 'groundspeak:name')
	cacheDesc = getTextFromDomElement( wpt, 'desc')
	print '-'*20
	print "Waypoint %s contains %d logs" % (wname, nrOfLogs)
	print "    cache: %s " % (cacheName)
 	print '    desc: ', cacheDesc
 	print "    lat: %s, lon: %s " % (wpt.attributes['lat'].value, wpt.attributes['lon'].value)
 	


def printLogEntry( logEntry ):
	logId = logEntry.attributes['id'].value
	logDate = getTextFromDomElement( logEntry, 'groundspeak:date')
	logType = getTextFromDomElement( logEntry, 'groundspeak:type')
	finder  = getTextFromDomElement( logEntry, 'groundspeak:finder')
	logText = getTextFromDomElement( logEntry, 'groundspeak:text' ) 
	#logText = logEntry.getElementsByTagName('groundspeak:text')[0].firstChild.wholeText
	print '     ', '- '*5
	print ' '*8, 'id = %s, %s, logdate = %s by %s, %s' % (logId, logType, logDate, finder, logText)



def getTextFromDomElement( domElement, elementName ):
	return domElement.getElementsByTagName( elementName )[0].firstChild.wholeText



dom = xml.dom.minidom.parse(filename)
waypoints=dom.getElementsByTagName('wpt')
printFileStatistics(dom, waypoints)



for wpt in waypoints:
	logs = wpt.getElementsByTagName('groundspeak:log')
	printWayPoint( wpt, logs.length )
	for log in logs:
		printLogEntry( log )
    
   