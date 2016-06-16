class Sensei:

    nombre = 'Paco'
    apellido = 'Ocampo'
    cinta = 'Roja'

    def __init__(self, nom): #ap):
        #if not char1:
            #pass
        #else:
        if nom == "":
            pass
        else:
            self.nombre = nom
        #self.apellido = ap

    def nombreCompleto(self):
        resultado = '{0} {1} {2}'.format(self.nombre, self.apellido, self.cinta)
        print(resultado)
'''
    def nombreCompleto():
        resultado = '{0} {1} {2}'.format(nombre, apellido, cinta)
        print(resultado)
'''

Sensei("").nombreCompleto()

Sensei('charlie').nombreCompleto()

#lass Main:
