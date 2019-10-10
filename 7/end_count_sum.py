sum = 0
a = 0
while a != 'stop':
    a = input ('Введите число: ')
    if a.isdigit():
        sum = sum + int(a)
    elif a == 'stop':
        print (sum)
    else:
        a = input('Ошибка! Введите число!: ')

