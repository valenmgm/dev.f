'''def multiply(n):
    if n >= 0:
        return(n * (5 ** len(str(n))))
    else:
        return(n * (5 ** (len(str(n))-1)))
    else:
        return(0)
'''


def multiply(n):
  return n*5**len(str(abs(n)))
