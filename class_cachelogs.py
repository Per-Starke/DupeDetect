__author__ = 'Per'
# 12.04.14
# works


class cachelogs(object):
    def __init__(self, cache):
        self.cache = cache
        self.logs = []

    def add_logentry(self, log):
        self.logs.append(log)

    def getLogs(self):
        return self.logs


