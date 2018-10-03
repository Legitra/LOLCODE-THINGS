'''
Type(s) of error:
    >Syntax, Logical
changes:
    >added some comments to explain whats happening
    >line 16: replaced the 7 so the pounds variable wasn't redundant
    >line 16: added braket before the multiply
    >line 18: replaced the plus with a comma because kgTotal is an int, not a str
'''

#script to convert weight in stone and pounds to kg
# 14 pounds in a stone and one stone is 6.35029kg

stone = 12                                  #Converting 12st and 7lbs
pounds = 7
kgTotal = ((pounds/14) + stone) * 6.35029   #converted pounds to stone, totaled the weight
                                            #then converted total to kg
print("Weight in kg: ", kgTotal)
