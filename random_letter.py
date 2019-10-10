import random
L = ['самовар', 'весна', 'лето']
slovo = L[random.randint(0, len(L)-1)]
bukva = random.randint(0, len(slovo)-1)
prost = list (slovo)[bukva]

vopros = list(slovo)
vopros[bukva]= '?'
print(' '.join(vopros))

x = input ('введите букву: ')

if x == prost:
    print ('победа!')
else:
    print ('Увы! Попробуйте еще раз!')
    print ('Слово: ', slovo)

    
