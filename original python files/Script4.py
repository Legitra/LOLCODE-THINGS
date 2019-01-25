# Books cost $20 each.  For every 10 ordered the 11th is free.
# Delivery is $10 for the first book and $2 for each additional book.
# What is the total cost cost for 80 books?

numBooks  = 80
freeBooks = 0

bookCost  = 20

for i in range(1,numBooks+1):               #Every 11th book is free
    if i % 11 == 0:
        freeBooks += 1

bookTotal = bookCost*(numBooks-freeBooks)   #Cost = all books - freebooks
deliveryTotal = 10 + 2*(numBooks-1)         #First book is $10 and all others are $2

totalCost = bookTotal + deliveryTotal       #Final cost
print("$" + str(totalCost))
