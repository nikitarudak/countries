from module import *
countries = {"Estonia": "Tallinn", "Lithuania": "Vilnus","Latvia": "Riga", "Finland": "Helsinki", "Sweden": "Stockholm", "Norway": "Oslo", "Germany": "Berlin", "Poland": "Warsaw", "France": "Paris", "England": "London", "Italy": "Rome", "Denmark": "Copenhagen"}
countr_list = readDictKeys(countries)
town_list = readDictVal(countries)

while True:
    menu = input("Перевод: название страны - столица - T\nДобавить новую страну/столицу - U\nИсправить ошибку - V\nСамостоятельная проверка - K\nСинтез речи (Google) - R\nВыход - L\n")
    if menu.upper() == "T":
        v = int(input("Название страны - столица / Столица - название страны (1/2): "))
        if v == 1:
            countr = input("Введите страну: ")
            basic = countr_list
            secondary = town_list
            t = translate(basic, secondary, countr.capitalize())
        elif v == 2:
            town = input("Введите город: ")
            basic = town_list
            secondary = countr_list
            t = translate(basic, secondary, town.capitalize())

        if t == False:
            ans = input("Добавить новую страну/столицу? y/n: ")
            if ans.lower() == "y":
                countr = input("Страна: ")
                town = input("Столица: ")
                newWord(countries, countr.capitalize(), town.capitalize())
                countr_list = readDictKeys(countries)
                town_list = readDictVal(countries)
            else:
                pass
    elif menu.upper() == "U":
        countr = input("Страна: ")
        town = input("Столица: ")
        newWord(countries, countr.capitalize(), town.capitalize())
        countr_list = readDictKeys(countries)
        town_list = readDictVal(countries)
        pass
    elif menu.upper() == "V":
        choice = int(input("Что исправить: столицу или страну? - 1/2: "))
        if choice == 1:
            lang1 = countr_list
            lang2 = town_list
            correction(lang1, lang2, choice, countries)
            town_list = readDictVal(countries)
        else:
            lang1 = town_list
            lang2 = countr_list
            correction(lang1, lang2, choice, countries)
            countr_list = readDictKeys(countries)
            town_list = readDictVal(countries)
        pass
    elif menu.upper() == "K":
        print("Проверка знания стран и их столиц".center(35, ))
        choice = int(input("Знание, что вы хотите проверить: знание стран или столиц? - 1/2: "))
        if choice == 1:
            lang1 = countr_list
            lang2 = town_list
            chekup(lang1, lang2)
        else:
            lang1 = town_list
            lang2 = countr_list
            chekup(lang1, lang2)
        pass
    elif menu.upper() == "R":
        ttsG()
    elif menu.upper() == "P":
        print(countr_list)
        print(town_list)
    else:
        print("Выход..")
        break
