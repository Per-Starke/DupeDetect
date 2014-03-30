__author__ = 'Per'
# 25.12.13
# working on it

from class_logentry import logentry
from class_cache import cache

class cachelogs(object):
    def __init__(self, cache):
        self.Cache = cache
        self.Logs = []

    def add_logentry(self, log):
        self.Logs.append(log)

    # def print(self):
    #     self.Cache.printcache()
    #     print()
    #     if len(self.Logs) >= 1:
    #         for log in self.Logs:
    #             print(log.printlog())
    #             print()

    # def getNrOfLogEntries(self):
    #     print(len(self.Logs))
    #
    # # def NoticeDupes(self):
    #     if len(self.Logs) > 1:
    #         print("Dupes detected!!!")
    #         self.Cache.printcache()
    #         print("It's logged with the following logs:")
    #         for log in self.Logs:
    #             log.printlog()
    #             print()
    #
    #     else:
    #         return("No dupes")
    #
    def getLogs(self):
        # end = len(self.Logs)
        # for i in range(0, end):
        #     print(self.Logs[i].printlog())
        return self.Logs


