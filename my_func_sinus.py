def f(x):
import math
if 0.2 <= x <= 0.9:
        return math.sin(x) 
    else: return 1
s = input('Введите число: ')
if s:
    print('F =',f(float(s)))
else: print('Введите число!')
