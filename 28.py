vstup = input('Zadaj text:')
sifra = ''
posun=int(input('zadaj posun'))

for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)+posun)
    if znak == 'z':
        novyznak = 'a'
    sifra = sifra+novyznak
print(sifra)
