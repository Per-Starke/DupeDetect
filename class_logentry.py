__author__ = 'Per'
# 12.04.14
# works


class logentry(object):
    def __init__(self, logid, logtype, logdate, logtxt):
        self.logid = logid
        self.logtype = logtype
        self.logdate = logdate
        self.logtxt = logtxt



    def printlog(self):
        return(self.logid, "logtype      :", self.logtype, "logdate      :", self.logdate, "logtext      :", self.logtxt[0:50] + "...")
        # print("log-ID       :", self.Logid)
        # print("logtype      :", self.Logtype)
        # print("logdate      :", self.Logdate)
        # print("logtext      :", self.Logtxt)

    # def logtype(self):
    #     return(self.Logtype)
    #
    # def logdate(self):
    #     return(self.Logdate)
    #
    # def logtxt(self):
    #     return(self.Logtxt)
    #
    # def logid(self):
    #     return(self.Logid)