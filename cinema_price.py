date = input ("введите дату: ")
film = input("введите название фильма: ")
time = int (input("выберите время: "))
person = int (input("количество билетов: "))
skidos = 1
if date == 'tomorrow':
    skidos = 0.95
if person > 19:
    skidos = 0.8
if person > 19 and date == 'tomorrow':
    skidos = 0.75

    
if film == 'friday':
        if time == 12:
            print (person * 250 * skidos)
        elif time == 16:
            print (person * 350 * skidos)
        elif time == 20:
            print (person * 450 * skidos)
elif film == 'championofdeath':
        if time == 10:
            print (person * 250 * skidos)
        elif time == 13:
            print (person * 350 * skidos)
        elif time == 16:
            print (person * 350 * skidos)
elif film == 'birdsband':
        if time == 10:
            print (person * 350 * skidos)
        elif time == 14:
            print (person * 450 * skidos)
        elif time == 18:
            print (person * 450 * skidos)
