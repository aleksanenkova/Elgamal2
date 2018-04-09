# -*- coding: utf-8 -*-
import random
#Тест Рабина-Миллера
#число p - простое, если выполняется одно из условий 1. (a^d)^2^r=−1(mod p) 2. a^d=1(mod p)

# производится g раундов проверки числа p на простоту
def base(p):
    i, j = 2, 0
#    пока i^2 <= p и j не равен 1
    while i*i <= p and j != 1:
#        если остаток р от деления на i равен 0, то j = 1
        if p%i == 0:
            j = 1
#        следущий раунд
        i += 1
#            если остаток 0, то число СОСТАВНОЕ
    if j == 1:
#    если не ок, то возращаем False
        return False
#   если все ок, то возращаем True
    else:
        return True

#Основная функция, считывает входной файл, считывает параметры, генерирует ключи
def Main(mess):
#def Keygen():
#Вывод таблицы символов
#начинаем с 11 чтоб таблица шифрования состояла из пар, а не по одному символу
    z, code = 11, {}
    for i in range (1040, 1072):
#        убираем нули, иначе ниче не получится, потому что при расшифрование будет неправильно считываться
        if z % 10 != 0:
            code[chr(i)] = z
#        если все ок, то идем дальше
        else:
            z += 1
            code[chr(i)] = z
        z += 1
#то что записано в файлике делаем капсом, чтоб считывался любой регистр
    mess = mess.upper()
#    если сивол есть в таблице символов, то берем его,
    for i in mess:
        if i not in code:
#            иначе заменяем "ничем"
            mess = mess.replace(i, '')
#    Генерация ключей
    print ("Генерация ключей\n")
#    просим ввести простое число
    p = int(input("Число p= "))
    while not base(p): p = int(input("Неверно! Введите p: "))
#    вызывается функция для вычисления g
    g = Square_root(p)
#    просим ввести число 1< x < = p
    x = int(input("Число x= "))
#если не подходит под условие, то нужно написать другое число
    while x <= 1 or x >= p: x = int(input("Неверно! Введите x: "))
#   вычисляем у по формуле
    y = pow(g, x, p)
#   открытым ключом является тройка (p,g,y)
    publicKey = [p, g, y]
#   печатаем открытый ключ
    print("Открытым ключом является тройка (p,g,y): ", publicKey)
#   закрытый ключ - число х
    privateKey = x
#   печатаем закрытый ключ
    print("Закрытый ключ: ", privateKey)
#   просим выбрать режим
    order = str(input("\n1. Encryption \n2. Decryption\n "))
#    print (order)
#   если выбрали 1
    if order == '1':
#def encode(mess):
# то шифруем
#выведем алфавит с таблицей шифрования
#l - код символа
        l = code.keys()
        l = list(l)
#        сортировка кодов
        l.sort()
#        для всех кодов сделаем красивый вывод на экран
        for i in l:
            print(i, '-', code[i], end = '  ')

#       делаем их строковыми переменными, иначе ничего не будет работать
#       для этого вводим новую переменную
        codemess = ''
        for i in mess:
#            запишем в нее все коды
            codemess += str(code[i])
#       выведем на экран как шифруется наше входное сообщение
        print('\nСообщение: "'+mess + '" шифруется как "' + codemess+'"')
#       теперь формируем пары
        cmp_p = str(p)
        tmp, f, pairs = '', 0, []
#       откроем файл для записи результата (криптограммы)
        f_out = open('output.txt', 'w')
        while f < len(codemess):
#            к - рандомно выбирается
            k = random.randint(2, p-2)
#            выведем к на экран
            print('k=', k)
    #       если длина нашего простого числа равна 1
            if len(cmp_p) == 1:
#                то буквы кодируются не по парам, а по одному, т к 1, 2, 3, 4, 5, 6, 7, 8, 9,
#                 состоят из одной цифры
                tmp = codemess[f]
                codetmp = int(tmp)
#               вычислим пары а и b   по формуле
                a, b = pow(g, k, p), pow(y, k) * codetmp % p
#               запишем в переменную pairs наши пары
                pairs.append([a, b])

#                Запишим их в файлик
                f_out.write(str(a)+' '+str(b)+'\n')
#                идем дальше
                f += 1
    #            print (len(cmp_p))
            else:
#                если длина всё таки больше 1
                tmp = codemess[f:f+len(cmp_p)]
                codetmp = int(tmp)

    #            print (p)
#                если сообщение для шифрования меньше числа р
                if codetmp <= p:
#               вычислим пары а и b   по формуле
                    a, b = pow(g, k, p), pow(y, k) * codetmp % p
#                   запишем в переменную pairs наши пары
                    pairs.append([a, b])
#                    Запишим их в файлик
                    f_out.write(str(a)+' '+str(b)+'\n')
#                    идем дальше
                    f += len(cmp_p)
#                    Для наглядности разбиения сообщения на пары сделаем вывод на экран
                    print ('M='+str(codetmp)+'\n')
#                если сообщение для шифрования больше числа р
                if codetmp >= p:
#                    берем только ОДНО число. Поэтому f+len(cmp_p)-1
                    tmp = codemess[f:f+len(cmp_p)-1]
#                    print (tmp)
                    codetmp = int(tmp)
#                    Для наглядности разбиения сообщения на пары сделаем вывод на экран
                    print ('M='+str(codetmp)+'\n')
#               вычислим пары а и b   по формуле
                    a, b = pow(g, k, p), pow(y, k) * codetmp % p
#                    Запишим их в файлик
                    f_out.write(str(a)+' '+str(b)+'\n')
#                   запишем в переменную pairs наши пары
                    pairs.append([a, b])
#                    идем дальше
                    f += len(cmp_p)-1
#                    f_out.close()
        print ('полученый шифротекст: ')
#       выведем криптограмму на экран
        print(pairs)
    else:
#        если мы выбрали режим ДЕШИФРОВАНИЯ
        f_dec = open('output.txt', 'r')
#        print (f_dec.read())
#       пустая переменная для записи нашего расшифрованного сообщения
        mess = []
#        считываем по одной паре
        for line in f_dec.readlines():
#            убираем не нужное, если бы оно было.
            line = line.replace(',', '')
#            и переходы тоже
            line = line.replace('\n', '')
#            разделим всё на "слова". split() делит строку на отдельные элементы между которыми есть пробел
            a = line.split()
#            переводим их в инт, а то не получится :)
            a[0], a[1] = int(a[0]), int(a[1])
#           запишем то что получилось по порядку.  append - добавить в конец строчки
            mess.append(a)
#            print("получилось :)")
#             теперь сделаем все в символы, чтобы было понятно
        z, code = 10, {}
        for i in range (1040, 1072):
            if z % 10 != 0: code[z] = chr(i)
            else:
                z += 1
                code[z] = chr(i)
            z += 1

#        print (mess)
#       выходное сообщение будем писать сюда
        outmess = ''
        for i in mess:
#            вычислем сообщение по формуле
            outmess += str(pow(i[0], p-1-x) * i[1] % p)
#        выведем сообщение в числовой форме
        print (outmess)
#        теперь финал. В буквенный вид
        finalOut = ''
        for i in range(0, len(outmess), 2):
#            смотрим по таблице шифрования что к чему
            tmp = int(outmess[i:i+2])
#            добавляем буквы в строку
            finalOut += code[tmp]
#        печатаем финальный результат в строку
        print(finalOut)

def Square_root(p):
    #вычисляем g
    euler_func = set(num for num in range (1, p))
    for g in range(2, p):
        current_func = set(pow(g, powers, p) for powers in range (1, p))

        if euler_func == current_func:
            return g
#файл для mess
f = open('input.txt', 'r')
mess = f.readline()
f.close()
Main(mess)
#input ()

