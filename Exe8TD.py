import random





candidat  = [ "Alexandre", "Clement ", "Leo",  ]

note      = [ "pas bien", " assez bien", " bien ", "tres bien ", "excellent"]

student = int(input(  "Enter number of student" ) )

vote      = []

alexandre = []

clement   = []

leo       = []




def select_random (candidat) :

    return random.choice(candidat)

#print ( "le nom choisi est ", select_random(candidat))


for i in  range (0, student) :

    vote.append ( select_random ( candidat ) )
    
    vote.append ( select_random ( note ) )
     

    if "Alexandre" in vote :  
        print ( "bon" )

        vote.remove( "Alexandre" )
        
    
        alexandre.append( vote [-1:] )

    
    

    if "Clement" in vote : 
        print ( "bonjour" )

        vote.remove( "Clement" )
        
    
        clement.append( vote [-1:] )

    


    if "Leo" in vote :
        print ( "bonsoir" )

        vote.remove( "Leo" )
        print ( vote)
    
        leo.append( vote [-1:] )

    


print ("liste d'alexandre",alexandre)
print ( "liste de leo",leo)
print ("liste de clement",clement)

print ( vote )



















