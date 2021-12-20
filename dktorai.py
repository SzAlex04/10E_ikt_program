print ('1. feladat.') 

print ('Jó napod van?')
napod = input('Milyen napod van?')

if napod == 'igen':
    print ('Örülök neki!')

elif napod == 'nem':
    print ('Hát ez szomorú!')
else:
    print ('Sajnos nem értem a válaszodat!')
    
print ('2. feladat')


print ('3. feladat')

from random import randrange
randomszam = randrange (1,5)
print ('Adj meg egy számot!')
bemenet = int(input)

if bemenet == randomszam:
    print ('Egyezik a két szám.')

elif bemenet > randomszam:
    print ('A megadott szám nagyobb, mint a random szám.')

else:
    print ('A megadott szám kisebb, mint a random szám.')    
