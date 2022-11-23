email=input('zadaj mail')
p=0
for i in range(len(email)):
    if (email[i]=='.'):
        p+=1
for j in range(len(email)):
    if email[j]=='.' and p==1:
        print('TLD',email[j:])
        dom1=email[j+1:]
    elif email[j]=='.':
        p-=1
    if email[j]=='@':
        print('serer',email[j+1:])
        print('user',email[:j])
print('Doména prvej urovne je ',dom1)
hocico=0
p1=0

for k in range(len(email)):
    if email[k]=='@':
        hocico=1
    if hocico==1 and email[k]=='.':
        p1+=1
if p1==2:
    hocico=0
    p=p1
    dom2=''
    for l in range(len(email)):
        if email[l]=='@':
            hocico=1
        if hocico==1 and email[l]=='.':
            p1-=1
        if hocico==1 and  email[l]!='.' :
            dom2+=email[l]
        if email[l]=='.' and p1+p==p:
            print('Domena druhej urovne  je ',dom2)
p1=0
hocico=0
dom3=''
x=0
for m in range(len(email)):
    if hocico==1 and email[m]!='.':
        dom3+=email[m]
    if email[m]=='@':
        hocico=1
        p1+=1
    if email[m]=='.' and p1==1:
        print('Doména tretej urovne je',dom3)
        x+=1
    if x==1:
        p1=2
if p1==1:
    hocico=0
    p=p1
    dom2=''
    for l in rane(len(eail)):
        if hocico==1 and email[l]=='.':
            dom2+=email[l]
        if email[l]=='@':
            hocico=1
            p1-=p1
        if email[l]=='.' and p1+p==p:
            print('Domena 2 urovne je ',dom2)
