'''
Type(s) of error:
    >Syntax, Logical
changes:
    >changed varible 'class' to 'class_total'
    >Line 16: changed 'male/class' to 'female/class'
'''

# The class has 44 students, 17 of whom are female.
# Script to find out the percentage female and male

class_total      = 44
female           = 17
male             = class_total - female
percentageMale   = male / class_total * 100
percentageFemale = female / class_total * 100

print('Class total is', class_total)
print('Percentage of class that is female is: ',percentageMale)
print('Percentage of class that is male is:   ',percentageFemale)
