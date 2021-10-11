x = int(input('Adj meg egy számot:'))
y = int(input('Add meg másik számot:'))
z = int(input('Add meg a harmadik számot:'))

a = min (x,y,z)

print ('A legkisebb szám!', a,)


x = int(input('Adj meg egy számot:'))
y = int(input('Add meg másik számot:'))
z = int(input('Add meg a harmadik számot:'))

a = max (x,y,z)

print ('A legnagyobb szám!', a,)


x = int(input('A pontszámod: '))
if(x<25):
    print ('Egyes, szia')
if(25<=x<50):
    print ('Kettes, már haladás')
if(50<=x<70):
    print ('Hármas, alakul')
if(75<=x<90):
    print ('nóNégyes, egész szép')
if(90<=x<=100):
    print ('Ötös, gratula')              


