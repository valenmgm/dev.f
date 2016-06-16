'''
def diamond(n):
    # Make some diamonds!
    if n%2 == 0:
        return()
    else:
        for resta in range(-(int((n-1)/2)), int(((n-1)/2) + 1)):
            print(abs(resta)*" " + (n-(2*abs(resta)))*"*" + abs(resta)*" ")
'''

def diamond(n):
    # Make some diamonds!
    result =""
    if n%2 == 0:
        return(None)
    else:
        for resta in range(-(int((n-1)/2)), int(((n-1)/2) + 1)):
            result += (str(abs(resta)*" " + (n-(2*abs(resta)))*"*") + "\n")
        print(result)

diamond(27)
