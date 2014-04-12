__author__ = 'Per'
# 12.04.14
# works


class logentry(object):
    def __init__(self, logid, logtype, logdate, logtxt):
        self.Logid = logid
        self.Logtype = logtype
        self.Logdate = logdate
        self.Logtxt = logtxt



    def printlog(self):
        return(self.Logid, "logtype      :", self.Logtype, "logdate      :", self.Logdate, "logtext      :", self.Logtxt[0:50] + "...")
        # print("log-ID       :", self.Logid)
        # print("logtype      :", self.Logtype)
        # print("logdate      :", self.Logdate)
        # print("logtext      :", self.Logtxt)

    def logtype(self):
        return(self.Logtype)

    def logdate(self):
        return(self.Logdate)

    def logtxt(self):
        return(self.Logtxt)

    def logid(self):
        return(self.Logid)