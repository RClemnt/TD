# Exercice 6

from random import *

win = 0

for i in range (0,100) :

    win = win -2
    des_1 = randint (1,4)
    des_2 = randint (1,4)

    if des_1 == des_2 : 

        win = win + des_1*2 + 2
        
print (win)




















