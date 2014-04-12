__author__ = 'Per'
# 12.04.14
# works


class cachelogs(object):
    def __init__(self, cache):
        self.Cache = cache
        self.Logs = []

    def add_logentry(self, log):
        self.Logs.append(log)

    def getLogs(self):
        return self.Logs


