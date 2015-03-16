import time
import datetime
#sample input: 2015-07-01 2015-07-04
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

























