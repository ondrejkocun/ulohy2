veta=input("napis vetu a ukonci ju bodkou")
poc=0
porad=0
najdlhsie=""
slovo=""
for i in veta:
    if i==' ' or i=='.':
        poc+=1
        if len(slovo)>len(najdlhsie):
            j=slovo
            porad=poc
        slovo=''
    else:
        slovo+=i
print('Pocet slov je ',poc)
print(len(najdlhsie),porad)
print(najdlhsie)
