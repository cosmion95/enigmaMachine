import random

# definire 3 rotoare si un reflector
# 95 de valori in total -> toate caracterele ascii incepand de la SPACE(32) pana la }(125)
# nu am inclus ultimul caracter din tabelul ascii ~(126) ca sa am un numar par de elemente pentru reflector

#stabilesc si legaturile, le-am generat random cu functiile de mai jos
r1 = [
   (0, 59), (1, 60), (2, 22), (3, 77), (4, 73), (5, 38), (6, 16), (7, 56), (8, 15), (9, 13), (10, 8), (11, 75),
   (12, 78), (13, 62), (14, 93), (15, 54), (16, 81), (17, 74), (18, 82), (19, 26), (20, 27), (21, 86),
   (22, 43), (23, 57), (24, 35), (25, 2), (26, 48), (27, 64), (28, 0), (29, 79), (30, 51), (31, 89),
   (32, 45), (33, 17), (34, 23), (35, 66), (36, 5), (37, 36), (38, 71), (39, 9), (40, 70), (41, 85),
   (42, 52), (43, 42), (44, 11), (45, 28), (46, 30), (47, 19), (48, 68), (49, 46), (50, 67), (51, 3),
   (52, 12), (53, 69), (54, 7), (55, 72), (56, 44), (57, 37), (58, 10), (59, 84), (60, 6), (61, 83),
   (62, 14), (63, 58), (64, 53), (65, 24), (66, 63), (67, 92), (68, 65), (69, 25), (70, 55), (71, 34),
   (72, 90), (73, 32), (74, 21), (75, 88), (76, 80), (77, 4), (78, 1), (79, 87), (80, 49), (81, 39),
   (82, 91), (83, 61), (84, 40), (85, 47), (86, 41), (87, 50), (88, 18), (89, 29), (90, 33), (91, 20),
   (92, 31), (93, 76), ]
r2 = [
   (0, 52), (1, 17), (2, 47), (3, 53), (4, 8), (5, 89), (6, 85), (7, 90), (8, 78), (9, 56), (10, 93), (11, 51),
   (12, 74), (13, 49), (14, 80), (15, 79), (16, 15), (17, 41), (18, 50), (19, 40), (20, 81), (21, 75),
   (22, 5), (23, 48), (24, 87), (25, 59), (26, 4), (27, 43), (28, 12), (29, 20), (30, 13), (31, 64),
   (32, 61), (33, 3), (34, 57), (35, 11), (36, 76), (37, 86), (38, 58), (39, 91), (40, 2), (41, 30),
   (42, 84), (43, 63), (44, 0), (45, 16), (46, 22), (47, 33), (48, 6), (49, 24), (50, 77), (51, 67),
   (52, 32), (53, 25), (54, 68), (55, 38), (56, 27), (57, 31), (58, 10), (59, 72), (60, 28), (61, 73),
   (62, 83), (63, 36), (64, 60), (65, 26), (66, 82), (67, 88), (68, 34), (69, 42), (70, 66), (71, 23),
   (72, 71), (73, 21), (74, 62), (75, 35), (76, 14), (77, 18), (78, 69), (79, 44), (80, 19), (81, 65),
   (82, 70), (83, 55), (84, 37), (85, 9), (86, 39), (87, 54), (88, 1), (89, 92), (90, 45), (91, 46),
   (92, 29), (93, 7), ]
r3 = [
   (0, 24), (1, 59), (2, 73), (3, 18), (4, 8), (5, 65), (6, 69), (7, 74), (8, 92), (9, 60), (10, 93), (11, 22),
   (12, 28), (13, 87), (14, 30), (15, 27), (16, 35), (17, 34), (18, 13), (19, 54), (20, 80), (21, 67),
   (22, 3), (23, 66), (24, 20), (25, 31), (26, 76), (27, 26), (28, 2), (29, 14), (30, 91), (31, 44),
   (32, 42), (33, 48), (34, 23), (35, 11), (36, 50), (37, 52), (38, 46), (39, 49), (40, 51), (41, 61),
   (42, 39), (43, 15), (44, 36), (45, 16), (46, 62), (47, 58), (48, 43), (49, 84), (50, 41), (51, 6),
   (52, 70), (53, 78), (54, 0), (55, 19), (56, 10), (57, 5), (58, 85), (59, 82), (60, 88), (61, 21),
   (62, 81), (63, 33), (64, 77), (65, 7), (66, 71), (67, 72), (68, 89), (69, 68), (70, 32), (71, 63),
   (72, 40), (73, 37), (74, 1), (75, 4), (76, 38), (77, 57), (78, 29), (79, 45), (80, 79), (81, 56),
   (82, 12), (83, 53), (84, 17), (85, 9), (86, 83), (87, 47), (88, 75), (89, 64), (90, 25), (91, 90),
   (92, 86), (93, 55), ]

reflector = [
   (65, 22), (45, 12), (5, 69), (44, 80), (67, 11), (54, 79), (90, 47), (40, 0), (84, 25), (78, 58), (85, 72), (39, 70),
   (57, 81), (59, 20), (56, 1), (36, 14), (15, 92), (23, 73), (2, 43), (29, 27), (32, 51), (61, 49),
   (37, 26), (89, 77), (41, 3), (30, 17), (48, 34), (66, 63), (38, 13), (74, 35), (76, 6), (68, 71),
   (28, 53), (31, 8), (21, 33), (7, 52), (60, 82), (88, 87), (16, 93), (4, 86), (24, 64), (42, 9),
   (18, 75), (46, 62), (19, 55), (50, 91), (83, 10), ]

links = [
   (66, 51), (61, 83), (43, 67), (70, 50), (62, 54), (86, 55), (47, 78), (71, 27), (77, 32), (23, 73), (75, 34), (4, 26),
   (29, 6), (57, 49), (3, 68), (0, 64), (18, 89), (36, 46), (33, 84), (19, 20), (11, 58), (22, 92),
   (81, 60), (7, 24), (85, 37), (41, 40), (59, 44), (69, 52), (30, 21), (91, 45), (80, 56), (10, 93),
   (13, 28), (48, 5), (17, 12), (38, 88), (25, 31), (39, 63), (53, 15), (87, 8), (35, 90), (1, 65),
   (42, 9), (72, 82), (76, 16), (2, 14), (74, 79), ]

# /////------- FUNCTII FOLOSITE NUMAI 1 DATA PENTRU GENERAREA LEGATURILOR DIN ROTOARE ---------- ///////
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
# //////////////-----------------------------------------------------------------///////////////

#pozitii de start ale rotoarelor: valoare intre 1 si 95
pozitieRotor1 = 1
pozitieRotor2 = 1
pozitieRotor3 = 1

rotatiiR1 = 1
rotatiiR2 = 1
rotatiiR3 = 1

rotireCompleta = 94

def findLink(key):
    for link in links:
        if link[0] == key:
            return link[1]
        if link[1] == key:
            return link[0]

def rotateRotor(rotor):
    for i in range(len(rotor)):
        if i == 0:
            previousValue = rotor[i][1]
        else:
            currentValue = rotor[i][1]
            rotor[i] = (rotor[i][0], previousValue)
            previousValue = currentValue
    rotor[0] = (rotor[0][0], previousValue)

def getValueFromRotors(key):
    #efectuez rotirea
    #verific daca vreun rotor se afla pe ultima pozitie
    if rotatiiR1%rotireCompleta == 0:
        #R2 trebuie rotit
        if rotatiiR2%rotireCompleta == 0:
            #R3 trebuie rotit
            rotateRotor(r3)
        rotateRotor(r2)
    rotateRotor(r1)

    # gasesc legatura din primul rotor
    for tup in r1:
        if tup[0] == key:
            outKey1 = tup[1]
            break
    # gasesc legatura din al doilea rotor
    for tup in r2:
        if tup[0] == outKey1:
            outKey2 = tup[1]
            break
    # gasesc legatura din al treilea rotor
    for tup in r3:
        if tup[0] == outKey2:
            outKey3 = tup[1]
            break

    # gasesc legatura din reflector
    for tup in reflector:
        if tup[0] == outKey3:
            refKey = tup[1]
            break
        if tup[1] == outKey3:
            refKey = tup[0]
            break

    # ma intorc inapoi prin rotoare
    for tup in r3:
        if tup[1] == refKey:
            outKey3 = tup[0]
            break
    for tup in r2:
        if tup[1] == outKey3:
            outKey2 = tup[0]
            break
    for tup in r1:
        if tup[1] == outKey2:
            outKey1 = tup[0]
            break

    return outKey1


def startEnigma():
    global pozitieRotor1
    global pozitieRotor2
    global pozitieRotor3

    global rotatiiR1
    global rotatiiR2
    global rotatiiR3

    newPozR1 = input("Introduceti pozitia de start pentru rotorul 1(ENTER=1): ")
    newPozR2 = input("Introduceti pozitia de start pentru rotorul 2(ENTER=1): ")
    newPozR3 = input("Introduceti pozitia de start pentru rotorul 3(ENTER=1): ")

    if newPozR1:
        pozitieRotor1 = int(newPozR1)
    if newPozR2:
        pozitieRotor2 = int(newPozR2)
    if newPozR3:
        pozitieRotor3 = int(newPozR3)

    #rotesc rotoarele pana ajung in pozitiile de start
    for i in range(pozitieRotor1):
        rotateRotor(r1)
        rotatiiR1 += 1
    for i in range(pozitieRotor2):
        rotateRotor(r2)
        rotatiiR2 += 1
    for i in range(pozitieRotor3):
        rotateRotor(r3)
        rotatiiR3 += 1

    #citesc inputul de la tastatura
    userInput = input("Introduceti textul care urmeaza sa fie criptat:\n")
    encryptedUserInput = ""
    for char in userInput:
        #obtin codul ascii
        inputAsciiValue = ord(char)

        #gasesc caracterul la care e legat
        # -32 fiindca in rotoare am inceput numaratoarea de la 0
        linkedAsciiValue = findLink(inputAsciiValue-32)

        #o trec prin cele 3 rotoare si reflector
        returnValue = getValueFromRotors(linkedAsciiValue)

        #gasesc caracterul la care e legat
        linkedReturnValue = findLink(returnValue)

        finalReturnValue = linkedReturnValue + 32

        #transform inapoi in char din cod ascii
        encryptedUserInput = encryptedUserInput + chr(finalReturnValue)

    print("Pentru decriptare rulati din nou programul folosind aceleasi setari de pornire.\nRezultatul criptarii:")
    print(encryptedUserInput)


startEnigma()