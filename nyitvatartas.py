time = int(input('Hány óra van?'))

if (8<time<16) :
    print ('Nyitva van a bolt.')
    print ('Még ennyi ideig van nyitva a bolt.', 16-time,'óra')

else :
    print ('A bolt zárva van.')
    print (32-time,'óra múlva lesz nyitva a bolt.')
