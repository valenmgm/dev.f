lista = ["a","b","c"]
categoria = ["alta", "media", "baja"]


#resultado = list(map(lambda elemL: str(elemL) + " ," + str([(element) for element in categoria]) ,lista))
resultado = [[elemL, palabraC] for elemL in lista for palabraC in categoria]
print()
print(resultado[0][1])
