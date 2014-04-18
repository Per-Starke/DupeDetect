__author__ = 'Per'
# 12.04.14
# works


class cache(object):
    def __init__(self, gccode, gcname):
        self.gccode = gccode
        self.gcname = gcname

    def printcache(self):
        return "Gccode       :", self.gccode, "Name         :", self.gcname


    # def gccode(self):
    #         return(self.Gccode)
    # def gcname(self):
    #     return(self.Gcname)


