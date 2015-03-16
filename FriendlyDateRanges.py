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

def assignTime(correctInput):
    separatedInput = []
    for entry in correctInput:
        for item in entry.split("-"):
            separatedInput.append(item)
    print(separatedInput)
    return separatedInput

correctInput = checkInput()
print(correctInput)
separatedInput = assignTime()
yearStart = int(separatedInput[0])
monthStart = int(separatedInput[1])
dayStart = int(separatedInput[2])
yearEnd = int(separatedInput[3])
monthEnd = int(separatedInput[4])
dayEnd = int(separatedInput[5])
includeYear = True
includeMonth = True
wrongInput = False

if (yearEnd-yearStart)<=1:
    if (yearEnd-yearStart)==1:
        if (monthEnd - monthStart)<0:
            includeYear = False
        elif (monthEnd == monthStart)==0:
            includeYear = False

    elif (yearEnd-yearStart)==0:
        includeYear = False
        if (monthEnd-monthStart)==0:
            if (dayEnd - dayStart)<0:
                wrongInput = True
        elif (monthEnd-monthStart)<0:
            wrongInput = True
    else:
        wrongInput = True


    if(yearEnd-yearStart)==1:
        if(monthEnd-monthStart)<=0:
            if monthEnd == monthStart:
                includeMonth = False
                inclueYear=False
        else:
            includeYear = False
    else:
        includeYear = False


def dayOutput(day):
    result = ""
    if day == 1 or day == 21 or day == 31:
        result = str(day)+"st"
    elif day == 2 or day == 22:
        result = str(day)+"nd"
    elif day == 3 or day == 23:
        result = str(day)+"rd"
    else:
        result = str(day)+"th"
    return result

def monthOutput(month):
    result = ""
    if month == 1:
        result = "January"
    if month == 2:
        result = "February"
    if month == 3:
        result = "March"
    if month == 4:
        result = "April"
    if month == 5:
        result = "May"
    if month == 6:
        result = "June"
    if month == 7:
        result = "July"
    if month == 8:
        result = "August"
    if month == 9:
        result = "September"
    if month == 10:
        result = "October"
    if month == 11:
        result = "November"
    if month == 12:
        result = "December"
    return result

outputYearStart = str(yearStart)
outputYearEnd = str(yearEnd)
outputMonthStart = monthOutput(monthStart)
outputMonthEnd = monthOutput(monthEnd)
outputDayStart = dayOutput(dayStart)
outputDayEnd = dayOutput(dayEnd)


































