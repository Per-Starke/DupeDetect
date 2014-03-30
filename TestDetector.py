"""
>>> from class_logentry import logentry
>>> from class_cachelogs import cachelogs
>>> from class_cache import cache

>>> le1 = logentry("found", 221212, "t4tc")

>>> le2 = logentry("found", 231212, "tftc")

>>> le3 = logentry("not found", 211212, "ooooch...")

>>> cache1 = cache("gctesti", "testcache", 2, 25, "this is the testcache")

>>> cache1.printcache()
Gccode       : gctesti
Name         : testcache
Dfficulty    : 2
Terrain      : 25
Description  : this is the testcache
>>> log1 = cachelogs(cache1)

>>> log1.add_logentry(le3)

>>> log1.print()
Gccode       : gctesti
Name         : testcache
Dfficulty    : 2
Terrain      : 25
Description  : this is the testcache
<BLANKLINE>
logtype      : not found
logdate      : 211212
logtext      : ooooch...
<BLANKLINE>

>>> log1.NoticeDupes()
No Dupe's detected
>>> log1.add_logentry(le1)

>>> log1.NoticeDupes()
Dupes detected!!!
Gccode       : gctesti
Name         : testcache
Dfficulty    : 2
Terrain      : 25
Description  : this is the testcache
It's logged with the following logs:
logtype      : not found
logdate      : 211212
logtext      : ooooch...
<BLANKLINE>
logtype      : found
logdate      : 221212
logtext      : t4tc
<BLANKLINE>

"""
