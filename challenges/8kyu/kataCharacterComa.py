def print_array(arr):
    resultado = ""
    for element in arr[:-1]:
        resultado = (resultado + str(element) +",")
    resultado = resultado + str(arr[-1])

    print(resultado)

    '''
    Resultado Paco:

        list = []
        for element in arr:
            list.append[element]

        print(",".join(list))

    '''
print_array(["a", "b", "xyz", "valentin", "l"])
