def pi(x):
    from math import pi
    return f'{pi:.{x}f}'
y = input ("Введите количество знаков после запятой: ")
if y:
    print (pi(y))
else:
    print ("Введите количество знаков после запятой!!:")
