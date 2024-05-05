import PrereqParser
import InitializeCourses

for i in InitializeCourses.courses:
    if PrereqParser.met(i):
        print(i)
print(PrereqParser.met(['CSI', '4900', 'summer', '$18|CSISEG|3:4']))
