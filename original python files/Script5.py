'''
Type(s) of error:
    >Syntax, Logical
changes:
    >Put speechmarks in the input
    >Lines 12 and 13: changed toprint to toPrint
'''

name = input('what is your name?')
repeatingLine = "Happy Birthday to You.\n"
toPrint = repeatingLine*2
toPrint = toPrint + "Happy Birthday dear " + str(name) + "\n"
toPrint = toPrint + repeatingLine

print(toPrint)
