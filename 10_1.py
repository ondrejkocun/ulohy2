from random import *
meno = input('Ako sa voláš?')
print('Ahoj '+meno+' rád Ťa spoznávam :)')
roknarodenia = input(meno+', v ktorom roku si sa narodil?')
riesenie=input("aké je tvoje obluene maďaraske radio")
meno2 = choice(('Alena', 'Barbora', 'Eva', 'Sofia'))
print('Á spomínam si, v roku '+roknarodenia+' sa narodila aj '+meno2)
print('Máš',2022-int(roknarodenia),' rokov a do sto rokov ti chýba',100-(2022-int(roknarodenia)),'rokov')
print("Rádio",riesenie,'je dost nevkusne bratku')
