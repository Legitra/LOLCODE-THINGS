#script to convert weight in stone and pounds to kg
# 14 pounds in a stone and one stone is 6.35029kg

stone = 12                                  #Converting 12st and 7lbs
pounds = 7
kgTotal = ((pounds/14) + stone) * 6.35029   #converted pounds to stone, totaled the weight
                                            #then converted total to kg
print("Weight in kg: ", kgTotal)
