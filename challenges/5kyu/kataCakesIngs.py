def cakes(recipe, available):

    '''
    class Ingridients(object):
        def __init__(self, **entries):
            self.__dict__.update(entries)

    recipeings = Ingridients(**recipe)
    for element in recipeings:
        print(element)
    '''

    lista = []
    for element in recipe:
        try:
            lista.append(available[element]//recipe[element])
        except(ZeroDivisionError, KeyError):
            print(0)
    print(min(lista))

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}



#def cakes(recipe, available):
 # return min(available.get(k, 0)/recipe[k] for k in recipe)
cakes(recipe,available)
