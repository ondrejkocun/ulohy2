vstup = input('Zadaj text:')
sifra = ''
desifra = " "
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)+1)
    if znak == 'z':
        novyznak = 'a'
    sifra = sifra+novyznak
print(sifra)

for znak in sifra:
    novyznak=znak
    if 'a'<=znak<='y':
        novyznak=chr(ord(znak)-1)
    if znak=='a':
        novyznak='z'
    desifra+=novyznak
print(desifra)
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)+2)
    if znak == 'z':
        novyznak = 'a'
    sifra = sifra+novyznak
print(sifra)

for znak in sifra:
    novyznak=znak
    if 'a'<=znak<='y':
        novyznak=chr(ord(znak)-2)
    if znak=='a':
        novyznak='z'
    desifra+=novyznak
print(desifra)
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)+3)
    if znak == 'z':
        novyznak = 'a'
    sifra = sifra+novyznak
print(sifra)

for znak in sifra:
    novyznak=znak
    if 'a'<=znak<='y':
        novyznak=chr(ord(znak)-3)
    if znak=='a':
        novyznak='z'
    desifra+=novyznak
print(desifra)
      
      
      
      
