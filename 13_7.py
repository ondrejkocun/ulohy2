slovo=""
meno=input("zaddaj slovo")
meno1=input("zaddaj slovo")
if len(meno)>len(meno1):
    dlzka=len(meno1)
else:
    dlzka=len(meno)
for i in range(dlzka):
    if i%2==0:
        slovo+=meno[i]
    else:
        slovo+=meno1[i]
print(slovo)
