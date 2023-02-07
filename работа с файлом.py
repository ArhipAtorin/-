from __future__ import print_function
import io, sys
while True:
    a = str(input("Тип телевизора(20-24; 30-32; 40; 42-43; 46-48; 49-50; 55-58; 60-65; 70+): "))
    print()
    if a == str("20-24"):
        b = str(input("Что вывести? Название и цену, название и артикуль или все: "))
        if b == str("название и артикуль") or b == str("Название и артикуль"):
            word = 'LED телевизоры 20-24'
            with io.open('2.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("название и цену") or b == str("Название и цену"):
            word = 'LED телевизоры 20-24'
            with io.open('3.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                        
                        
        if b == str("все") or b == str("Все"):
            word = 'LED телевизоры 20-24'
            with io.open('1.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")

                        
    if a == str("30-32"):
        b = str(input("Что вывести? Название и цену, название и артикуль или все: "))
        if b == str("название и артикуль") or b == str("Название и артикуль"):
            word = 'LED телевизоры 30-32'
            with io.open('2.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("название и цену") or b == str("Название и цену"):
            word = 'LED телевизоры 30-32'
            with io.open('3.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("все") or b == str("Все"):
            word = 'LED телевизоры 30-32'
            with io.open('1.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")

                        
    if a == str("40"):
        b = str(input("Что вывести? Название и цену, название и артикуль или все: "))
        if b == str("название и артикуль") or b == str("Название и артикуль"):
            word = 'LED телевизоры 40'
            with io.open('2.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("название и цену") or b == str("Название и цену"):
            word = 'LED телевизоры 40'
            with io.open('3.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("все") or b == str("Все"):
            word = 'LED телевизоры 40'
            with io.open('1.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")

                        
    if a == str("42-43"):
        b = str(input("Что вывести? Название и цену, название и артикуль или все: "))
        if b == str("название и артикуль") or b == str("Название и артикуль"):
            word = 'LED телевизоры 42-43'
            with io.open('2.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("название и цену") or b == str("Название и цену"):
            word = 'LED телевизоры 42-43'
            with io.open('3.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("все") or b == str("Все"):
            word = 'LED телевизоры 42-43'
            with io.open('1.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")

                        
                    
    if a == str("46-48"):
        b = str(input("Что вывести? Название и цену, название и артикуль или все: "))
        if b == str("название и артикуль") or b == str("Название и артикуль"):
            word = 'LED телевизоры 46-48'
            with io.open('2.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("название и цену") or b == str("Название и цену"):
            word = 'LED телевизоры 46-48'
            with io.open('3.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("все") or b == str("Все"):
            word = 'LED телевизоры 46-48'
            with io.open('1.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")


                        
    if a == str("49-50"):
        b = str(input("Что вывести? Название и цену, название и артикуль или все: "))
        if b == str("название и артикуль") or b == str("Название и артикуль"):
            word = 'LED телевизоры 49-50'
            with io.open('2.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("название и цену") or b == str("Название и цену"):
            word = 'LED телевизоры 49-50'
            with io.open('3.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("все") or b == str("Все"):
            word = 'LED телевизоры 49-50'
            with io.open('1.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")


                        
    if a == str("55-58"):
        b = str(input("Что вывести? Название и цену, название и артикуль или все: "))
        if b == str("название и артикуль") or b == str("Название и артикуль"):
            word = 'LED телевизоры 55-58'
            with io.open('2.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("название и цену") or b == str("Название и цену"):
            word = 'LED телевизоры 55-58'
            with io.open('3.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("все") or b == str("Все"):
            word = 'LED телевизоры 55-58'
            with io.open('1.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            

                        
    if a == str("60-65"):
        b = str(input("Что вывести? Название и цену, название и артикуль или все: "))
        if b == str("название и артикуль") or b == str("Название и артикуль"):
            word = 'LED телевизоры 60-65'
            with io.open('2.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("название и цену") or b == str("Название и цену"):
            word = 'LED телевизоры 60-65'
            with io.open('3.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
                            
        if b == str("все") or b == str("Все"):
            word = 'LED телевизоры 60-65'
            with io.open('1.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")

                        
    if a == str("70+"):
        b = str(input("Что вывести? Название и цену, название и артикуль или все: "))
        if b == str("название и артикуль") or b == str("Название и артикуль"):
            word = 'LED телевизоры 70 +'
            with io.open('2.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
        if b == str("название и цену") or b == str("Название и цену"):
            word = 'LED телевизоры 70 +'
            with io.open('3.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
        if b == str("все") or b == str("Все"):
            word = 'LED телевизоры 70 +'
            with io.open('1.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print(line, end='' "\n")
                        with open('text.txt', 'a') as f:
                            f.write(line)
                            print("Текст был сохронен")
##    print("РЕКЛАМА: ссылка на мой github со всеми работами: https://github.com/ArhipAtorin")
    print()
    v = str(input("Вывести список команд?(да)/(нет): "))
    if v == str("Да") or v == str("да"):
        print("end - конец работы")
        print()
        print("return - заново начать работу")
        g = str(input(""))
        if g == str("end") or g == str("End"):
            print('Работа окончена')
            break
        if g == str("return") or g == str("Return"):
            print("Хорошо")
        if v == str("нет") or v == str("Нет"):
            print("Хорошо")

