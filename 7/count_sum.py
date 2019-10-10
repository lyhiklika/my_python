import math
b = 0
sum = 0
a = int( input('Введите число: ')
while a > 0:
    if a % 10 // 2 == 1:
        b = a % 10
    a = a // 10
    sum = sum + pow(b)
print (sum)
    
