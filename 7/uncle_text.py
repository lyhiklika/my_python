s = '''Мой дядя самых честных правил,
     Когда не в шутку занемог,
     Он уважать себя заставил
     И лучше выдумать не мог'''
k = 0 
uncle = ' ' 
for i in range(len(s)): 
    if k == 0: 
        if s[i]=='м' and s[i-1] == ' ': 
            k = 1 
        else: 
            uncle = uncle + s[i] 
    else: 
        if s[i] == ' ': 
            k = 0 
print(uncle)
