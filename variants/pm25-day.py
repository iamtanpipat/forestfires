#Gets one day PM 2.5 figure. The day can be given as a parameter. If no parameter, it's the day before yesterday
#Marko Niinimaki niinimakim@webster.ac.th 2020
#The optional paramter's format is 2020-01-30
#The output file is datepm25.nc, for example 2020-01-30pm25.nc
#!/usr/bin/env python
import datetime
import sys
from ecmwfapi import ECMWFDataServer

now = datetime.datetime.now()

today = datetime.date.today()
yday = today - datetime.timedelta(days=2)

year = yday.year
month = yday.month
day = yday.day

monthstr = str(month)
daystr = str(day)

if month < 10:
    monthstr = "0" + str(month)

if day < 10:
    daystr = "0" + str(day)

if day < 10:
    daystr = "0" + str(day)

if len(sys.argv) == 2:
    dstr = sys.argv[1]
else:
    dstr = str(year)+"-"+monthstr+"-"+daystr\

print dstr

#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "mc",
    "dataset": "cams_gfas",
    "date": dstr,
    "expver": "0001",
    "levtype": "sfc",
    "param": "87.210",
    "step": "0-24",
    "stream": "gfas",
    "time": "00:00:00",
    "format": "netcdf",
    "type": "ga",
    "target": dstr+"pm25.nc",
})
