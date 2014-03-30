"""
>>> from class_logentry import logentry
>>> from class_cachelogs import cachelogs
>>> from class_cache import cache

>>> cache1 = cache("gctesti", "testcache")

>>> cache1.printcache()
Gccode       : gctesti
Name         : testcache
>>> cache1.gccode()
'gctesti'
>>> cache1.gcname()
'testcache'
>>> le1 = logentry(1234, "found", 210113, "asfd")

>>> le1.printlog()
(1234, 'logtype      :', 'found', 'logdate      :', 210113, 'logtext      :', 'asfd...')
>>> le2 = logentry(2345, "found", 220214, "asdfjld")

>>> log1 = cachelogs(cache1)

>>> log1.add_logentry(le1)

#>>> log1.getNrOfLogEntries()
#1
#>>> log1.print()
#Gccode       : gctesti
#Name         : testcache
#<BLANKLINE>
#(1234, 'logtype      :', 'found', 'logdate      :', 210113, 'logtext      :', 'asfd...')
#<BLANKLINE>
>>> log1.add_logentry(le2)

#>>> log1.getNrOfLogEntries()
#2
#>>> log1.print()
#Gccode       : gctesti
#Name         : testcache
#<BLANKLINE>
#(1234, 'logtype      :', 'found', 'logdate      :', 210113, 'logtext      :', 'asfd...')
#<BLANKLINE>
#(2345, 'logtype      :', 'found', 'logdate      :', 220214, 'logtext      :', 'asdfjld...')
#<BLANKLINE>
>>> le1.logtype()
'found'
>>> le1.logdate()
210113
>>> le1.logtxt()
'asfd'

"""
