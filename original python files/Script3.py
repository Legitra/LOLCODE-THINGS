# The class has 44 students, 17 of whom are female. None are nonbinary.
# Script to find out the percentage female and male

class_total      = 44
female           = 17
male             = class_total - female
percentageMale   = male / class_total * 100
percentageFemale = female / class_total * 100

print('Class total is', class_total)
print('Percentage of class that is female is: ',percentageMale)
print('Percentage of class that is male is:   ',percentageFemale)
