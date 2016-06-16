#Nombres específicos para variables
x = 0
#While mejor que For
for i in range(1000):
    #Definir min i
    if mod i/3 == 0:
        #Mod se escibe % y como operador entre números
        x += i
#Usar Or para tener un solo If
    elif mod i/5 == 0:
        x = x+1
        i = i+1

print(x)
