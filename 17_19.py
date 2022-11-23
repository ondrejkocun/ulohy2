url=input('zadaj url')
for i in range(len(url)):
    if url[i]==':':
        print(url[0:i])
p=''
poc=0
bod=0
for j in range(len(url)):
    if url[j]=='/':
           poc = poc + 1
    if (url[j] == "/") and (poc == 3):
        print(p)
    if (poc == 2) and not (url[j] == "/"):
        p = p + url[j]
    if (poc == 2) and (url[j] == "."):
        bod = bod + 1
 
dn = " "
poc_b = 0
for k in range(len(url)):
    if url[k] == ".":
        poc_b = poc_b + 1
        
    if (url[k] == "/") and (poc_b == bod):
        print(dn)
    if (poc_b == bod) and not (url[k] == "."):
        dn = dn + url[k]
