#-*- encoding utf-8 -*-
#país niña
'''
def iterarLista(lista):
    sqrs =[]
    for element in lista:
        sqrs.append(element ** 2)

    print(sqrs)

iterarLista([1,2,3,4,5])
'''
###############################################################

def cuadrados(num):
    return(num **2)

print(cuadrados(6))

lista = [1,2,3,4,5,6,7,8,9,10]

squares = list(map(cuadrados, lista))

print(squares)

#################################################################

def holaAlumno(nombre):
    return "Hola " + nombre
alumnos = ["Rinay", "Valentin", "Adriana"]
print(list(map(holaAlumno, alumnos)))

###################################################

#deffuncion(x):
#    return x * 10


def pordiez(x):
    return(x * 10)
# = (lambda x: x * 10)
print(list(map(pordiez, range(1,6))))
