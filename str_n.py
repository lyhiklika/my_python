def f(s,n):
    if len(s) > n:
        return (s.upper ())
    else :
        return s
s = input ('введите строку: ')
n = int(input ('введите значение n: '))
if s:
    if n:
        print (f(s,n))
    else:
     print   ('введите число n!')
else:
  print  ('введите строку!')
