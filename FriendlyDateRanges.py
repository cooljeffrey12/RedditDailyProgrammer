import time
#sample input: 2015-07-01 2015-07-04
def checkInput():
    verifyInput = False
    correctInput = []
    while verifyInput == False:
        dateInput = input("Type in two dates in YYYY-MM-DD format separated by space \n")
        listInput = dateInput.split(" ")
        for entry in listInput:
            try:
                correctInput.append(time.strptime(entry, "%Y-%m-%d"))
            except ValueError:
                print("ValueError. Wrong input. Type in input again")
            #else:
        if len(listInput) == 2:
            verifyInput = True
        else:
            print("You only typed in", len(listInput), "date(s). Two dates required.")
    print("Input Success!")
    return correctInput

correctInput = checkInput()
print(correctInput)















