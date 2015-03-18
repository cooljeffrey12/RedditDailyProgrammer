while selectorCorrect == False:
    selector = input("Type V for ISBN Validator or G for ISBN Generator. Type Q to quit\n")
    if (selector == "v" or selector == "V"):
        inputCorrect = False
        while inputCorrect == False:
            inputISBN = input("Type in a 10-digit ISBN code\n")
            if len(inputISBN) == 10 and inputISBN[9] in ["0","1","2","3","4","5","6","7","8","9","x","X"]:
                inputCorrect = True
        firstNine = inputISBN[:9]
        lastDigit = inputISBN[9]
        multiplier = 10
        sum = 0
        for digit in firstNine:
            sum = sum + (int(digit) * multiplier)
            multiplier = multiplier - 1
        if lastDigit == "x" or lastDigit == "X":
            sum = sum + 10
        elif lastDigit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            sum = sum + int(lastDigit)
        if sum%11 == 0:
            print(inputISBN, "is valid")
        else:
            print(inputISBN, "is NOT valid")
    # elif selector == "g" or selector == "G":
    elif selector == "q" or selector == "Q":
        selectorCorrect = True