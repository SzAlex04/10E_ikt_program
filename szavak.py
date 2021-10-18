szo1 = input('Adj meg egy szót')
szo2 = input('Adj meg egy másikat is')

szo1_hossza = len(szo1)
szo2_hossza = len(szo2)

if szo1_hossza>szo2_hossza:
    print ('A hosszabb szó a',szo1,)

elif szo1_hossza==szo2_hossza :
    print ('A két szó egyforma hosszú')

else:
    print ('A hosszabb szó a',szo2,)         