# example xml reader for gpx files
import xml.dom.minidom

# from xml.dom.minidom import Node

filename = 'test-cachelist.xml'

def printWayPoint( wpt ):
 	print "lat: %s, lon: %s " % (wpt.attributes['lat'].value, wpt.attributes['lon'].value)
 	print 'name: ', wpt.getElementsByTagName('name')[0].firstChild.wholeText
 	print 'desc: ', wpt.getElementsByTagName('desc')[0].firstChild.wholeText



dom = xml.dom.minidom.parse(filename)

waypoints=dom.getElementsByTagName('wpt')

print 'file %s contains %d waypoints' % (filename, waypoints.length)

caches = dom.getElementsByTagName('groundspeak:cache')
print '... and %d caches' % (caches.length)

print '='*50 

for wpt in waypoints:
	printWayPoint( wpt )
	logs = wpt.getElementsByTagName('groundspeak:log')
	print "waypoint contains %d logs" % (logs.length)
    
   