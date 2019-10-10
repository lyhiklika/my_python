s = "У лукоморья 123 дуб зеленый 456"
print ("позиция буквы я в строке: ", s.find ("я"))
print ("буква у встречается " , s.count ("у"), " раз в строке ")
if s.isalpha() == False:
    print (s.upper())
if len (s) > 4:
    print ( s.lower () )
print ( "o" + s[1:])
