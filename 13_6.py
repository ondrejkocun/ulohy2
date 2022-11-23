slovo=input("zaddaj slovo")
meno=""
meno1=""
for i in  range(len(slovo)):
    if i%2==0:
        meno+=slovo[i]
    else:
        meno1+=slovo[i]
print(meno)
print(meno1)
