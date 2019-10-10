x = int (input ("введите код города"))
y = float(input("введите длительность разговора"))
if x:
    if y:
        if x == 343:
            print (15 * y)
        elif x == 381:
            print (18 * y)
        elif x == 473:
            print (13 * y)
        elif x == 485:
            print (11 * y)
    else:
        print ("введите код города!!")
else:
    print ("введите длительность разговора!!")
