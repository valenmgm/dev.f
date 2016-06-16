def multiplication_table(row,col):
    lista = []
    for fila in range(1, row+1):
        lista.append(map(lambda columna: (columna * fila), range(1, col+1)))
    return(lista)

    #return[[(r+1)*(c+1) for c in range(col) for r in range(row)]

'''
    lista = []
    subset = []
    def agregar_subset(fila)
        subset.append(columna*fila)
    for columna in range(1, col+1):
        map(agregar_subset, range(1, row+1))
        lista.append(subset)
        subset=[]
    print(lista)
'''

multiplication_table(3,3)
multiplication_table(3,4)
multiplication_table(4,3)
