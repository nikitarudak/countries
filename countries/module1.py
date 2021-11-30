from random import *
from gtts import gTTS
import os
def readDictVal(dic: dict)->list:
    """
    Читает значения из словаря и добавляем их в список
    :param dict dic: Название словаря
    """
    mas = []
    for v in dic.values():
        mas.append(v.strip(''))
    return mas

def readDictKeys(dic: dict)->list:
    """
    Читаем ключи из словаря и добавляем их в список
    :param dict dic: Название словаря
    """
    mas = []
    for v in dic.keys():
        mas.append(v.strip(''))
    return mas

def newWord(dic: dict, x: str, y: str):
    """
    Добавляем новую страну и столицу в словарь и список
    :param dict dic: Название словаря
    :param str x: Добавляемая страна
    :param str y: Добавляемая столица
    """
    dic.setdefault(x, y)

def wordSearch(n: str, l: list):
    """
    Ищем слово в списке
    Возвращает True или False
    :param str n: ищет логин
    :rtype: bool
    """
    if n in l:
        t = True
    else:
        t = False
    return t
    

def translate(lang1: list, lang2: list, word: str):
    """
    Ищем индекс слова в списке и выводим его перевод
    Возвращает False, если такого значения нет в списке
    :param list lang1: Первый список
    :param list lang2: Второй список
    :param str word: Страна/столица
    """
    t = wordSearch(word, lang1)
    if t == True:
        index1 = lang1.index(word)
        transword = lang2[index1]
        print(f"Перевод: {transword}")
    else:
        print("Такой страны/столицы нет в списке")
        return False

def correction(lang1: list, lang2: list, choice: int, dic: dict):
    """
    Ищем слово в файле и исправляем его
    :param list lang1: Первый список
    :param list lang2: Второй список
    :param int choice: Выбор пользователя
    :param dict dic: Словарь
    """
    print("Введите то, что хотите исправить".center(70, ))
    if choice == 1:
        wordup = input("Страна: ")
        word = wordup.capitalize()
        check = wordSearch(word, lang1)
    else:
        wordup = input("Столица: ")
        word = wordup.capitalize()
        check = wordSearch(word, lang1)

    if check == False:
        print("Такой страны/столицы нет в списке!")
    else:
        wordindex = lang1.index(word)
        transword = lang2[wordindex]
        print(f"Изначальный вариант - {transword}")
        print("Введите заменяемое слово".center(50, ))
        if choice == 1:
            replaceup = input("Столица: ")
            replace = replaceup.capitalize()
            dic[word] = replace
            print("Ошибка изменена".center(45, ))
        else:
            replaceup = input("Страна: ")
            replace = replaceup.capitalize()
            dic[replace] = dic.pop(transword)
            print("Ошибка исправлена".center(45, ))

def chekup(lang1: list, lang2: list):
    """
    Проверяет правильность перевода слов у пользователя
    :param list lang1: Список первого языка
    :param list lang2: Список второго языка
    """
    r = 0
    i = 0
    print("Вам будет даваться по пять слов за один раз. Дается слово и рядом нужно написать его значение\nПосле написания слова будет показано, правильный ли перевод. В конце вы узнаете результат по знанию этих слов")
    while True:
        for i in range(5):
            word = choice(lang1)
            index = lang1.index(word)
            transword = lang2[index]
            chek = input(f"{i+1}. {word} - ")
            if chek == transword:
                i += 1
                r += 1
                print("Перевод верный")
            else:
                i += 1
                print("Перевод неверен")
        result = r/i * 100
        print(f"Ваш результат: {r} правильных ответов, {result}%")
        ans = input("Закончить? y/n ")
        if ans.lower() == "y":
            break

def ttsG():
    '''
    Синтез речи от Google
    '''
    #from playsound import playsound #pip install
    print("Синтез речи".center(24, ))
    lang = int(input("На каком языке воспроизводить речь? рус/англ - 1/2: "))
    blabla = input("Введите слово: ")
    if lang == 1:
        tts = gTTS(text=blabla, lang="ru")
        tts.save("test.mp3")
    else:
        tts = gTTS(text=blabla, lang="eng")
        tts.save("test.mp3")
    os.system("test.mp3")
