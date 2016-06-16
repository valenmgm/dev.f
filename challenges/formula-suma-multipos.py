
def suma_multiplos(multiplo1, multiplo2, rangomin, rangomax, resultado):
    for  n in (rangomin, rangomax):
        if n % multiplo1 == 0 or n % multiplo2 == 0:
            resultado = resultado + n
            print(resultado)
    print(resultado)

suma_multiplos(3,5,1,18, 0)
