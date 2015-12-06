from transliterate import translit, get_available_language_codes
def Translit_from_russian(text):
    return translit(text,'ru',reversed=True)
def Translit_from_english(text):
    return translit(text,'ru')
def main():
    print ('1.Перевод из кириллицы в латиницу')
    print ('2.Перевод из латиницы в кириллицу')
    print ('3.Выход')
    z = int(input('Введите пункт меню:'))
    while z < 3:
        
        if z == 1:
            a = input('Введите русское предложение: ')
            print ('Ваше новое предлжение: ',Translit_from_russian(a))
        elif z == 2:
            a = input('Введите предложение на кириллице: ')
            print ('Ваше новое предложение: ', Translit_from_english(a))
        print ()
        print ('1.Перевод из кириллицы в латиницу')
        print ('2.Перевод из латиницы в кириллицу')
        print ('3.Выход')
        z = int(input('Введите пункт меню:'))
main()



        
                                               

            
            
    

