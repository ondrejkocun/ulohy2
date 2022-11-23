import random
heslo=''
rytmus=random.randrange(8)
for i in range(8):
    x=random.randrange(97,122)
    heslo+=chr(x)
print(heslo)
for i in range(len(heslo)):
    if i==rytmus:
        pismeno=chr(ord(heslo[i])-32)
        heslo1=heslo[:i]+pismeno+heslo[i+1:]
print(heslo1)
