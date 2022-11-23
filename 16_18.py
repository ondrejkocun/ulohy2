cislo=input('napis rodne cislo')
rok=cislo[0:2]
mesiac=cislo[2:4]
den=cislo[4:6]
datum=''
if int(mesiac)>12:
    mesiac=int(mesiac)-50
    pohlavie='zena'
else:
    pohlavie='muz'
if int(rok)>21:
    datum = den+" ."+str(mesiac)+" ."+"19"+rok
else:
    datum=den+" ."+str(mesiac)+" ."+"20"+rok
print('rodne cislo',cislo)
print('Datum narodenia',datum)
print(pohlavie)
