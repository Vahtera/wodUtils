import random
random.seed()

def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y

def randomValue(valMin, valMax):
    l = 0
    res = 0
    intValue = 0
    for i in range(4):
        l = random.randint(1, 5)
        res = res + l
    intValue = int(mapFromTo(res, 4, 20, valMin, valMax))
    return intValue

def intToDots(lInt):
    lString = ""
    for i in range(lInt):
        lString = lString + "•"
    if (lInt == 0):
        lString = "-"
    return lString

print()
print("Random Goon")
print("-----------")
print("Physical: " + intToDots(randomValue(0,6)))
print("Mental:   " + intToDots(randomValue(0,6)))
print("Social:   " + intToDots(randomValue(0,6)))
print()
print("Close Combat:        " + intToDots(randomValue(0,6)))
print("Ranged Combat:       " + intToDots(randomValue(0,6)))
print("Willpower:           " + intToDots(randomValue(0,6)))
print("Special Ability 1:   " + intToDots(randomValue(0,6)))
print("Special Ability 2:   " + intToDots(randomValue(0,6)))

#○⦿○⚪⚫