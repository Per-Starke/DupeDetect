__author__ = 'Per'
# 27.12.13
# working on it

from class_logentry import logentry
from class_cachelogs import cachelogs
from class_cache import cache
import pickle as p




cache1 = cache("GC2VTPZ", "Testcache")

cache = cache1.gccode()

le1 = logentry(337628572, "found", 221212, "sjfkjsdafiesjfksadfskadfjsadfasdfsadfsadfasdfsdfasdfjsdafjksdjfsdjfldsakjfkasdj"
                                "flkadsjfklasdjfkldsajfklasdjfklsdajflksadjfklasdaj"
                                "skdfjksdjfklasdjflksadjfklasdjfakldsjfadklsöfjlka"
                                "sdjfklasdjfklasdf")
le2 = logentry(337628559, "found", 231212, "tftc")
le3 = logentry(1234, "not found", 231214, "Not found :-(")
log1 = cachelogs(cache1)
log1.add_logentry(le1)
log1.add_logentry(le2)
log1.add_logentry(le3)


x = log1.getLogs()
i = len(x)

if i >= 2:
    fo = open("DupeDetectWeb.html", "w")
    fo.write("<html>\n <head>\n<title>  GC DupeDetect </title>\n <link href='DupeDetectColors.css' rel='stylesheet'/> \n"
             "</head>\n<body>\n<img src='./img/dupedetect.png' hight='45'/>\n"
             " <h2>\n<a href='http://coords.info/" + cache + "'target='blank'> Cache " + cache +
             "</a>\n</h2>")
else:
    fo = open("DupeDetectWeb.html", "w")
    fo.write("<html>\n <head>\n<title>  GC DupeDetect </title>\n  <link href='DupeDetectColors.css' rel='stylesheet'/> \n"
             "</head>\n<body>\n<img src='./img/dupedetect.png' hight='45'/>\n <h3 style='background-color: red; color: blue'> No dupes detected! </h3>")


if i >= 2:
    fo.write(" \n <h3 > These are the logs:  </h3> \n")
    for log in log1.Logs:
        x = str(log.printlog())
        y = str(log.logid())
        fo.write(" <h4> <a href='http://www.geocaching.com/seek/log.aspx?LID=" + y + "'target='blank'> "+ x +" </a>""</h4> \n")

fo.write("\n</body>\n</html>")
fo.close
