def valid_parentheses(string):
    lista = []
    for element in string: lista.append(element)
    if string == "":
        return(True)
    if lista.count("(") == lista.count(")"):
        if lista.index("(") < lista.index(")"):
            lista.reverse
            if lista.index(')') < lista.index('('):
                lista.reverse
                return(True)

    else:
        return(False)


valid_parentheses( "()(())()" )
