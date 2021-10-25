import random





candidat  = [ "Alexandre", "Clement", "Leo",  ]

note      = [  " bien ", "tres bien ", "excellent"]

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

        leo.append( vote [-1:] )
        vote.remove( "Leo" )



print ("liste d'alexandre",alexandre)
print ( "liste de leo",leo)
print ("liste de clement",clement)
print ( vote )


a = len ( alexandre )
c = len ( clement )  
l = len ( leo )

if a == c or a == l or c == l :

    a == alexandre.count ( "excellent" )

    c == clement.count ( "excellent" )

    l == leo.count ( "excellent" )



















