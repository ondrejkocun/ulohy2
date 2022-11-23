import random
heslo=''
for i in range(8):
    if i<3:
        x = random.randrange(65, 91)
        heslo+= chr(x)
    if 5>i>3:
        x=random.randrange(48,58)
        heslo+= chr(x)
    if i>5:
        x = random.randrange(97, 122)
        heslo+= chr(x)
print(heslo)
