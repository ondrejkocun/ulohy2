slovo=input("zadaj slovo")
hocico=''
for i in range(len(slovo)+1):
    print(hocico)
    hocico=''
    for j in range(len(slovo)):
        if i==j:
            hocico+=slovo[i]
        else:
            hocico+=' '
