hocico=97
volaco=''
for i in range(26):
    if hocico<122:
        volaco+=chr(hocico)+','
    else:
        volaco+=chr(hocico)
    hocico+=1
print(volaco)
