selector = input("Type V for ISBN Validator or G for ISBN Generator\n")
selectorCorrect = False


while selectorCorrect == False:
    if (selector == "v" or selector == "V"):
        selectorCorrect = True
        inputCorrect = False
            inputISBN = input("Type in a 10-digit ISBN code\n")
            if len(inputISBN) == 10:
                try:
                    int(selector.replace[:9])
                except TypeError:
                    print("First 9-digit needs to be an integer")
                else:
                    inputCorrect = True
        print(inputISBN)            # elif (selector == "g" or selector == "G"):
