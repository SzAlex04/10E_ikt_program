while True:

    valasz = input( 'Melyik nap van?')

    try:
        if valasz=="hétfő":
         print('Hétköznap van. 1.nap')
         break
        if valasz=="kedd":
         print('Hétköznap van. 2.nap')
         break
        if valasz=="szerda":
         print('Hétköznap van. 3.nap')
         break
        if valasz=="csütörtök":
         print('Hétköznap van. 4.nap')
         break
        if valasz=="péntek":
         print('Hétköznap van. 5.nap')
         break       
        if valasz=="szombat":
         print('Hétvége van. 6.nap')
         break
        if valasz=="vasárnap":
         print('Hétvége van. 7.nap')
         break    
        else:
            print('Nem írod jól!',end="")

    except Exception:
        print('Error.')

