# example xml reader for gpx files
import xml.dom.minidom

# from xml.dom.minidom import Node

filename = 'test-cachelist.xml'

def printWayPoint( wpt, nrOfLogs ):
	wname = wpt.getElementsByTagName('name')[0].firstChild.wholeText
	print "Waypoint %s contains %d logs" % (wname, nrOfLogs)
 	print '    desc: ', wpt.getElementsByTagName('desc')[0].firstChild.wholeText
 	print "    lat: %s, lon: %s " % (wpt.attributes['lat'].value, wpt.attributes['lon'].value)
 	print '-'*10, "\n"

def printFileStatistics( dom, waypoints ):
	nrOfLogs = dom.getElementsByTagName('groundspeak:log').length
	nrOfCaches = dom.getElementsByTagName('groundspeak:cache').length

	print "\n"*3
	print "File Statistics:"
	print 'file %s contains %d waypoints, %d caches and %d logs.' % (filename, waypoints.length, nrOfCaches, nrOfLogs)
	print '='*70, "\n"



dom = xml.dom.minidom.parse(filename)
waypoints=dom.getElementsByTagName('wpt')
printFileStatistics(dom, waypoints)



for wpt in waypoints:
	logs = wpt.getElementsByTagName('groundspeak:log')
	printWayPoint( wpt, logs.length )
    
   