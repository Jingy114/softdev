'''
Jing Feng, Anna Fang, Prattay Dey
SoftDev
04_choose
2022-09-22
time spent: 
DISCO:
- You can have multiple key-value pairs for an index
- You can access a specific value by entering its index after the key 
- Using randint will return integers while simply using random will return floats 
QCC:
OPS SUMMARY:
- We're thinking of importing the random python library for our RNG
- We're thinking of using randint(a,b) twice. 
    - The first time we'll use it to find a random key
    - The 2nd time we'll find a random value within that key
- We will have two methods
    - The first method will use random to generate the class (2/7/8) that the random dev will be selected from
    - The next will use random to provide the index of a randomly selected dev inside of the selected class
'''

import random as rng

krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
         }


def generateRandomDev():
    keys = list(krewes.keys())
    randIndex = rng.randint(0, len(krewes) - 1)
    randKey = keys[randIndex]
    fullPeriod = krewes[randKey]
    selectedDevo = rng.randint(0, len(fullPeriod)-1)
    return str(randKey) + ": " + fullPeriod[selectedDevo]

print( generateRandomDev() )
