__author__ = 'Per'
# 25.12.13
# works, extendable

class cache(object):
    def __init__(self, gccode, gcname):
        self.Gccode = gccode
        self.Gcname = gcname

    def printcache(self):
        print("Gccode       :", self.Gccode)
        print("Name         :", self.Gcname)


    def gccode(self):
            return(self.Gccode)
    def gcname(self):
        return(self.Gcname)


