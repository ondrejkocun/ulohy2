import random
heslo=''
for i in range(8):
    x=random.randrange(97,122)
    heslo+=chr(x)
print(heslo)
