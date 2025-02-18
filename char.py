import random
random.seed()

arrPron = ["She/Her", "She/Her", "She/Her", "He/Him", "He/Him", "He/Him", "They/Them"]
arrRace = ["Hunter", "Garou", "Vampire", "Changeling", "Wraith", "Bastet", "Mage"]
arrTribe = ["Bone Gnawer", "Stargazer", "Silver Fang", "Shadowlord", "Fianna", "Black Fury", "Red Talon", "Wendigo", "Silent Strider"]
arrKith = ["Sluagh", "Sidhe", "Troll", "Pooka", "Red Cap", "Boggan", "Eshu", "Nocker", "Satyr"]
arrBTribe = ["Bagheera", "Simba", "Balam", "Bubasti", "Khan", "Pumonca", "Qualmi", "Swara", "Hellcat"]
arrSphere = ["Prime", "Time", "Correspondence", "Mind", "Spirit", "Forces", "Entropy", "Life", "Matter"]
arrTradition = ["Celestial Chorus", "Cult of Ecstacy", "Virtual Adept", "Akashic Brotherhood", "Dreamspeaker", "Order of Hermes", "Euthanatos", "Verbena", "Sons of Ether"]
arrSpecial = ["Conviction", "Rage", "Blood", "Glamour", "Essence", "Rage", "Arete"]
arrClan = ["Ventrue", "Lasombra", "Toreador", "Tzimisce", "Gangrel", "Brujah", "Nosferatu", "Tremere", "Malkavian"]
arrDisc = ["Dominate", "Obtenebration", "Presence", "Vicissitude", "Animalism", "Celerity", "Obfuscate", "Thaumaturgy", "Dementation"]
arrDisc2 = ["Fortitude", "Dominate", "Auspex", "Animalism", "Potence", "Potence", "Potence", "Auspex", "Auspex"]
arrDisc3 = ["Presence", "Potence", "Celerity", "Auspex", "Prsence", "Presence", "Animalism", "Dominate", "Obfuscate"]

intSpecial = random.randint(0,8)
intRaceChance = random.randint(1,100)
intPron = random.randint(0,len(arrPron) - 1)
intRace = random.randint(0,len(arrRace) - 1)
intHumanLimit = 90
attrLimit  = 1

if (intRaceChance > intHumanLimit):
    raceOther = True
    attrLimit = 7
else:
    raceOther = False
    attrLimit = 5

print()
print("Random Character")
print("================")
print()
print("Pronouns : " + arrPron[intPron])

if (raceOther):
    if (arrRace[intRace] == "Garou"):
        print("Race     : " + arrRace[intRace] + " (" + arrTribe[intSpecial] + ")")
    elif (arrRace[intRace] == "Bastet"):
        print("Race     : " + arrRace[intRace] + " (" + arrBTribe[intSpecial] + ")")
    elif (arrRace[intRace] == "Changeling"):
        print("Race     : " + arrRace[intRace] + " (" + arrKith[intSpecial] + ")")
    elif (arrRace[intRace] == "Mage"):
        print("Race     : " + arrRace[intRace] + " (" + arrTradition[intSpecial] + ")")
    elif (arrRace[intRace] == "Vampire"):
        print("Race     : " + arrRace[intRace] + " (" + arrClan[intSpecial] + ")")
    else:
        print("Race     : " + arrRace[intRace])
else:
    print("Race     : Human")

print()

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

print("Physical : " + intToDots(randomValue(1,attrLimit)))
print("Mental   : " + intToDots(randomValue(1,attrLimit)))
print("Social   : " + intToDots(randomValue(1,attrLimit)))
print()
print("Close Combat    : " + intToDots(randomValue(0,attrLimit)))
print("Ranged Combat   : " + intToDots(randomValue(0,attrLimit)))
print("Willpower       : " + intToDots(randomValue(0,attrLimit)))
if (raceOther):
    print('{:15}'.format(arrSpecial[intRace]) + " : " + intToDots(randomValue(0,attrLimit)))
    if (arrRace[intRace] == "Vampire"):
        print('{:15}'.format(arrDisc[intSpecial]) + " : " + intToDots(randomValue(0,attrLimit)))
        print('{:15}'.format(arrDisc2[intSpecial]) + " : " + intToDots(randomValue(0,attrLimit)))
        print('{:15}'.format(arrDisc3[intSpecial]) + " : " + intToDots(randomValue(0,attrLimit)))
    elif (arrRace[intRace] == "Mage"):
        print('{:15}'.format(arrSphere[intSpecial]) + " : " + intToDots(randomValue(0,attrLimit)))
    elif (arrRace[intRace] == "Garou"):
        print('{:15}'.format("Gnosis") + " : " + intToDots(randomValue(0,attrLimit)))
    elif (arrRace[intRace] == "Bastet"):
        print('{:15}'.format("Gnosis") + " : " + intToDots(randomValue(0,attrLimit)))
    else:
        print("Special Ability : " + intToDots(randomValue(0,attrLimit)))

print()
print()
