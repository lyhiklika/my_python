def f(x):
    if 0.2 <=x<= 0.9:
        import math
        return math.sin(x) 
    else: return 1
s = input('Введите число: ')
if s:
    print('F =',f(float(s)))
else: print('Введите число!')
