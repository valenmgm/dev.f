def perms(element):
    import math

    combinaciones = (len(str(element)))
    repetidos = 1

    for character in set(str(element)):
        if str(element).count(character) > 1:
            repetidos = (repetidos * math.factorial(str(element).count(character)))

    print(math.factorial(combinaciones) / repetidos)


perms("abc")
perms("abb")
perms("aabb")
perms("aaab")
perms(737)
