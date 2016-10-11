import holidays
import datetime


def hoursdict(startdate, enddate):
    us_holidays = holidays.UnitedStates()
    date1 = datetime.datetime.strptime(startdate, "%m/%d/%Y").date()
    date2 = datetime.datetime.strptime(enddate, "%m/%d/%Y").date()
    day = datetime.timedelta(days=1)

    hoursDict = {}

    while date1 <= date2:
        monthdate = datetime.date(date1.year, date1.month, 1)
        formatteddate = monthdate.strftime('%m/%d/%Y')
        hoursDict.setdefault(formatteddate, {'PEAK': 0, 'OFFPEAK': 0})
        #print date1.strftime('%m/%d/%Y')
        if date1 in us_holidays or date1.isoweekday() == 6 or date1.isoweekday() == 7:
            hoursDict[formatteddate]['PEAK'] += 0
            hoursDict[formatteddate]['OFFPEAK'] += 24
        else:
            hoursDict[formatteddate]['PEAK'] += 16
            hoursDict[formatteddate]['OFFPEAK'] += 8

        date1 = date1 + day

    return hoursDict

startdate = '1/1/2016'
enddate = '12/1/2016'

x = hoursdict(startdate, enddate)
for each in x:
    print each