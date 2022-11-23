slovo=input('napis slovo')
slovo1=input('napis slovo')
if len(slovo)>len(slovo1):
    dlhsie=slovo
    kratsie=slovo1
else:
    dlhsie=slovo1
    kratsie=slovo
for i in range(len(dlhsie)):
    print(dlhsie[i],end='')
    if i<len(kratsie):
          print(kratsie[i],end='')
