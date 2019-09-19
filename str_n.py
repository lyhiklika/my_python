def f(s,n):
    if len(s)>n:
        return (s.upper ())
    else :
        return s
s=input ('введите строку: ')
n=int(input ('введите значение n: '))
if s:
    if n:
        print (f(s,n))
    else:
        ('введите число n!')
else:
    ('введите строку!')
