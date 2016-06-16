def climb(n):

    operations = []
    resultados = [1]

    while n != 1:
        if n%2 == 0:
            operations.append("a")
            n = n/2
        else:
            operations.append("b")
            n = (n-1)/2
    operations.reverse()

    for option in operations:
            if option == "a":
                resultados.append(resultados[-1]*2)
            elif option == "b":
                resultados.append(resultados[-1]*2 +1)

    print(resultados)
    
climb(100)
