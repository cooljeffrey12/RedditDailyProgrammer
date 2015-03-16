#sample input: 2015-07-01 2015-07-04
#sample_output: July 1st - 4th
# The goal of this challenge is to implement a way of converting two dates into a more friendly date
# range that could be presented to a user. It must not show any redundant information in the date range.
# For example, if the year and month are the same in the start and end dates, then only the day range should be displayed.
# Secondly, if the starting year is the current year, and the ending year can be inferred by the reader, the year
# should be omitted also (see below for examples).

import time
import datetime

def checkInput():
    verifyInput = False
    while verifyInput == False:
        dateInput = input("Type in two dates in YYYY-MM-DD format separated by space \n")
        listInput = dateInput.split(" ")
        for entry in listInput:
            try:
                time.strptime(entry, "%Y-%m-%d")
            except ValueError:
                print("ValueError. Wrong input. Type in input again")
            #else:
        if len(listInput) == 2:
            verifyInput = True
        else:
            print("You only typed in", len(listInput), "date(s). Two dates required.")
    print("Input Success!")
    return listInput

def getMonth(month):
    months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
    return months[month-1]

def getDay(day):
    result = ""
    if (day >= 10 and day < 20):
        result = str(day)+"th"
    elif day%10 == 1:
        result = str(day)+"st"
    elif day%10 == 2:
        result = str(day)+"nd"
    elif day%10 == 3:
        result = str(day)+"rd"
    else:
        result = str(day)+"th"
    return result

startDate, endDate = checkInput()
startYear = int(startDate[:4])
startMonth = int(startDate[5:7])
startDay = int(startDate[8:])
endYear = int(endDate[:4])
endMonth = int(endDate[5:7])
endDay = int(endDate[8:])

if (startYear == endYear):
    if startMonth == endMonth and startDate != endDate and startYear == 2015:
        print("%s %s - %s" % (getMonth(startMonth), getDay(startDay), getDay(endDay)))
    elif startMonth == endMonth and startDate != endDate:
        print("%s %s - %s, %s" % (getMonth(startMonth), getDay(startDay), getDay(endDay), str(startYear)))
    elif startMonth == endMonth and startDate == endDate and startYear==2015:
        print("%s %s" % (getMonth(startMonth), getDay(startDay)))
    elif startMonth == endMonth and startDate == endDate:
        print("%s %s, %s" % (getMonth(startMonth), getDay(startDay), str(startYear)))
    elif startMonth != endMonth and startYear==2015:
        print("%s %s - %s %s" % (getMonth(startMonth), getDay(startDay), getMonth(endMonth), getDay(endDay)))
    elif startMonth != endMonth:
        print("%s %s - %s %s, %s" % (getMonth(startMonth), getDay(startDay), getMonth(endMonth), getDay(endDay), str(startYear)))

elif endYear-startYear == 1:
    if endMonth < startMonth and startYear == 2015:
        print("%s %s - %s %s" % (getMonth(startMonth), getDay(startDay), getMonth(endMonth), getDay(endDay)))
    else:
        print("%s %s, %s - %s %s, %s" % (getMonth(startMonth), getDay(startDay), str(startYear), getMonth(endMonth), getDay(endDay), str(endYear)))

else:
    print("%s %s, %s - %s %s, %s" % (getMonth(startMonth), getDay(startDay), str(startYear), getMonth(endMonth), getDay(endDay), str(endYear)))

































