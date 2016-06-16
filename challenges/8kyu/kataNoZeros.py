def no_boring_zeros(n):
    if n == 0:
        print (n)
    else:
        n = str(n)
        while n[-1] == "0":
            n = n[:-1]
        print(int(n))
'''
        list = []
        result = ""
        for digit in str(n):
            list.append(digit)
        while list[-1] == "0":
            list.remove(list[-1])
        result = int("".join(list))

        print(result)
'''

no_boring_zeros(1050)
