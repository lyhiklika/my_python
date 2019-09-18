import random
x=random.randint (1,4)
y=int (input ("введите случайное число от 1 до 4: "))
if y==x:
    print ("Победа!")
elif y>x:
    print ("твое число больше загаданного\n Повтори еще раз: ")
else:
    print ("твое число меньше загаданного\n Повтори еще раз:")
    
