meno=input('Zadaj meno')
meno1=input('Zadaj meno')
slovo=''
p=len(meno)+len(meno1)
for i in range(p):
    if i%2==0:
        slovo+=meno[i//2]
    else:
        slovo +=meno1[i//2]
print(slovo)
