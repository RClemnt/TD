from random import *






# Exercice 3






    
ordi = randint ( 1,100 )

print ( ordi )

user = int(input("Enter number 1 à 100: "))

while user != ordi :

    try :
        if user < ordi :

            print ( "Trop petit ")

            user = int(input("Enter number : "))

        elif user > ordi :

            print ( "Trop grand ")

            user = int(input("Enter number : "))
          
    except : print("ERROR")

print( "Bravo")

# 4 

















































