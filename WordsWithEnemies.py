leftWord, rightWord = input("Type in two words separated by space in lower case \n").split(" ")
collectMiddle = []
for leftChar in leftWord:
    if leftChar in rightWord:
        leftWord = leftWord.replace(leftChar, "", 1)
        rightWord = rightWord.replace(leftChar, "", 1)
        collectMiddle.append(leftChar)

result = ""
if (len(leftWord) == len(rightWord)):
    result = "Tie."
elif (len(leftWord) > len(rightWord)):
    result = "Left wins."
else:
    result = "Right wins."

print(result, "Letters exploded:", collectMiddle)
