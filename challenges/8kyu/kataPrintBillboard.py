def billboard(name, *price):

    total = 0

    if not price:
        for i in range(1,len(str(name))+1):
            total += 30
    else:
        for i in range(1,len(str(name))+1):
            total += int(price[0])

    print(total)


    #multiplication, but try not to be lame and solve the kata in another way!
billboard("valen", 5)
