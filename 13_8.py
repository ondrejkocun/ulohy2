veta=input("zadaj vetu")
dlzka=len(veta)
for i in range(dlzka):
    if veta[i]==".":
        print('oznamovacia')
    if veta[i]=="?":
        print('opytovacia')
    if veta[i]=='!':
        print('rozkazovacia')
