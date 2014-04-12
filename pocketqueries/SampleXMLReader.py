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
	wname = wpt.getElementsByTagName('name')[0].firstChild.wholeText
	print '-'*20
	print "Waypoint %s contains %d logs" % (wname, nrOfLogs)
 	print '    desc: ', wpt.getElementsByTagName('desc')[0].firstChild.wholeText
 	print "    lat: %s, lon: %s " % (wpt.attributes['lat'].value, wpt.attributes['lon'].value)
 	

def printLogEntry( logEntry ):
	logId = logEntry.attributes['id'].value
	logDate = logEntry.getElementsByTagName('groundspeak:date')[0].firstChild.wholeText
	logType = logEntry.getElementsByTagName('groundspeak:type')[0].firstChild.wholeText
	finder  = logEntry.getElementsByTagName('groundspeak:finder')[0].firstChild.wholeText
	print '     ', '- '*5
	print ' '*8, 'id = %s, %s, logdate = %s by %s' % (logId, logType, logDate, finder)




dom = xml.dom.minidom.parse(filename)
waypoints=dom.getElementsByTagName('wpt')
printFileStatistics(dom, waypoints)



for wpt in waypoints:
	logs = wpt.getElementsByTagName('groundspeak:log')
	printWayPoint( wpt, logs.length )
	for log in logs:
		printLogEntry( log )
    
   