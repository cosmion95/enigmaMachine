import random

length = 93

def generateRotor():
    chosenNumbers = []
    x = "r1 = [\n" + "   "
    for i in range(length+1):
        numberFound = False
        while not numberFound:
            findLink = random.randint(0, length)
            foundOne = False
            if findLink != i:
                for chosenNumber in chosenNumbers:
                    if chosenNumber == findLink:
                        foundOne = True
                if not foundOne:
                    numberFound = True
        chosenNumbers.append(findLink)
        tup = (i, findLink)
        x = x + str(tup) + ", "
        if i%10 == 1 and i != 1:
            x = x + "\n" + "   "
    x = x + "]"
    return x

def generateReflector():
    chosenNumbers = []
    string = "reflector = [\n" + "   "
    for i in range(int((length+1)/2)):
        found = False
        while not found:
            exists = False
            x = random.randint(0, length)
            for n in chosenNumbers:
                if n == x:
                    exists = True
            if not exists:
                found = True
        chosenNumbers.append(x)

        found = False
        while not found:
            exists = False
            y = random.randint(0, length)
            for n in chosenNumbers:
                if n == y:
                    exists = True
            if not exists:
                found = True
        chosenNumbers.append(y)
        tup = (x, y)
        string = string + str(tup) + ", "
        if i % 10 == 1 and i != 1:
            string = string + "\n" + "   "
    string = string + "]"
    return string
