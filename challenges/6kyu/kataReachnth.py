def sumDig_nthTerm(initVal, patternL, nthTerm):
    lista = [initVal]
    iteration = 0
    result = 0
    while iteration < nthTerm:
        for addition in patternL:
                lista.append(lista[-1] + addition)
                iteration += 1
    for digit in str(lista[nthTerm - 1]):
        result += int(digit)
    print(result) #sum of digits of nthTerm of the generated sequence

sumDig_nthTerm(10, [1, 2, 3], 15)
