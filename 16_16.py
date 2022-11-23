hocico=input('vojta conga')
opacne=hocico[::-1]
for i in range(len(hocico)):
    volaco='.'*(len(hocico)-i)+opacne[len(hocico)-i-1:]+hocico[:i+1]+'.'*(len(hocico)-i)
    print(volaco)
