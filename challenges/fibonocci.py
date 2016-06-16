def fibonacci(n):
    listaFib = [0,1]
    for i in range(1,n):
        fibn = listaFib[-1] + listaFib[-2]
        listaFib.append(fibn)
    print(listaFib[n])

def start():
    try:
        n = input("Que Fibonacci necesitas?")
        fibonacci(int(n))
        eleccion()
    except:
        print("Intenta con un numero")
        start()

def eleccion():
    eleccion = input("Quieres otro Fibonacci(Si/No)")
    if eleccion == "Si" or "No":
        if eleccion == "Si":
            start()
        else:
            quit()
    else:
        print("Input invalido")
        start(eleccion)


start()
