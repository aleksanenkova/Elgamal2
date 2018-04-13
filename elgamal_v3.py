# -*- coding: utf-8 -*-
import random
import sys
import decimal
decimal.getcontext().prec = 100
#Тест Рабина-Миллера
# производится r_ раундов проверки числа p на простоту
def base(p, r_):
    if (p <=1):
        return False
    if (p == 2):
 
        return False
    if (p%2 == 0 or p%5 == 0 or p < 11 ):
 
        return False

    s = 0
    d = p - 1
    i = 0
    j = 0
    while (d% 2 == 0):
        d = d/2
        s+=1

    for a in range(r_):
        a = random.randint(2, p - 1)
#        print (a)
        x = (a**d)%p
#        print(x)
        if (x == 1 or x == p - 1):
            continue
            for j in range (s-1):
                x_sq = (x*x)%p
#                print (x_sq)
                if (x_sq == 1):
                    return False
                if (x_sq == p - 1):
                    break
            if (x != p - 1):
                return False
    return True

##    пока i^2 <= p и j не равен 1
#    while i*i <= p and j != 1:
##        если остаток р от деления на i равен 0, то j = 1
#        if p%i == 0:
#            j = 1
##        следущий раунд
#        i += 1
##            если остаток 0, то число СОСТАВНОЕ
#    if j == 1:
##    если не ок, то возращаем False
#        return False
##   если все ок, то возращаем True
#    else:
#        return True

#Основная функция, считывает входной файл, считывает параметры, генерирует ключи
def Main(mess):
#def Keygen():
#Вывод таблицы символов
#начинаем с 11 чтоб таблица шифрования состояла из пар, а не по одному символу
    code = {'А': 11, 'Б': 12, 'В': 13, 'Г':14, 'Д':15, 'Е':16, 'Ё':17, 'Ж':18, 'З':19, 'И':21, 'Й':22, 'К':23, 'Л':24, 'М':25, 'Н':26, 'О':27, 'П':28, 'Р':29, 'С':31, 'Т':32, 'У':33, 'Ф':34, 'Х':35, 'Ц':36, 'Ч':37, 'Щ':38, 'Ш':39, 'Ъ':41, 'Ь':42, 'Ы':43, 'Э':44, 'Ю':45, 'Я':46, '.':47, ',':48, '^':51, '!':52, '?':53, '*':54, '1':55, '2': 56, '3':57, '4':58, '5':59, '6':61, '7':62, '8':63, '9':64, '0':65}
    ALPH = u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЩШЫЬЪЭЮЯ1234567890.,^!?*'
    mess_ = u''
    for sym in mess.upper():
        if sym.upper() in ALPH:
            #        print alp[(sym).encode('utf-8')]
            mess_ += sym
    print (mess_)
#то что записано в файлике делаем капсом, чтоб считывался любой регистр
    mess = mess_.upper()
#    если сивол есть в таблице символов, то берем его,
    for i in mess:
        if i not in code:
#            иначе заменяем "ничем"
            mess = mess.replace(i, '')
    order = str(input("\n1. Keygen \n2. Encryption \n3. Decryption\n"))
    if order == '1':
    #    Генерация ключей
        print ("Генерация ключей\n")
    #    просим ввести простое число
        r_ = 20
        p = int(input("Число p= "))
        
        
        while not base(p, r_):
            p = int(input("Это число не подойдет для шифрования. Введите другое\nЧисло p= "))
        
        
        f_pk = open('pk.txt', 'w')
        f_pk.write(str(p)+' ')
    #    вызывается функция для вычисления g
        g = Square_root(p)
        f_pk.write(str(g)+' ')
    #    просим ввести число 1< x < = p
        x = random.randint(2, p-2)
        f_pk.write(str(x)+' ')
    #если не подходит под условие, то нужно написать другое число
        while x <= 1 or x >= p: x = int(input("Неверно! Введите x: "))
    #   вычисляем у по формуле
        y = int((g**x)%p)
        f_pk.write(str(y)+' ')
    #   открытым ключом является тройка (p,g,y)
        publicKey = [p, g, y]
    #   печатаем открытый ключ
        print("Открытым ключом является тройка (p,g,y): ", publicKey)
    #   закрытый ключ - число х
        privateKey = x
    #   печатаем закрытый ключ
        print("Закрытый ключ: ", privateKey)
    #   просим выбрать режим

#    print (order)
#   если выбрали 1
    if order == '2':
#def encode(mess):
# то шифруем
#выведем алфавит с таблицей шифрования
#l - код символа
        f_pk = open('pk.txt', 'r')
        pk = f_pk.read()
        pk = pk.split()

        p = int(pk[0])
        g = int(pk[1])
        x = int(pk[2])
        y = int(pk[3])
        
        l = code.keys()
        l = list(l)
#        сортировка кодов
        l.sort()
#        для всех кодов сделаем красивый вывод на экран
        for i in l:
            print(i, '-', code[i], end = ' \n')

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
        f_out = open('cryptogram.txt', 'w')
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
                a, b = (g**k)%p, ((y**k)%p * codetmp) % p
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
                if codetmp < p:
#               вычислим пары а и b   по формуле
                    a, b = (g**k)%p, ((y**k)%p * codetmp) % p
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
                    a, b = (g**k)%p, ((y**k)%p * codetmp) % p
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
    if order == '3':
        f_pk = open('pk.txt', 'r')
        pk = f_pk.read()
        pk = pk.split()
            
        p = int(pk[0])
        g = int(pk[1])
        x = int(pk[2])
        y = int(pk[3])
#        если мы выбрали режим ДЕШИФРОВАНИЯ
        f_dec = open('cryptogram.txt', 'r')
#        cryptogr = f_dec.read()

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
        code_2 = {11: 'A', 12: 'Б', 13: 'В', 14:'Г', 15:'Д', 16:'Е', 17:'Ё', 18:'Ж', 19:'З', 21:'И', 22:'Й', 23:'К', 24:'Л', 25:'М', 26:'Н', 27:'О', 28:'П', 29:'Р', 31:'С', 32:'Т', 33:'У', 34:'Ф', 35:'Х', 36:'Ц', 37:'Ч', 38:'Щ', 39:'Ш', 41:'Ъ', 42:'Ь', 43:'Ы', 44:'Э', 45:'Ю', 46:'Я', 47:'.', 48:',', 51:'^', 52:'!', 53:'?', 54:'*', 55:'1', 56: '2', 57:'3', 58:'4', 59:'5', 61:'6', 62:'7', 63:'8', 64:'9', 65: '0'}
            
 
        f_dec = open('cryptogram.txt', 'r')
        print ("Криптограмма:")
        print (f_dec.read())
        print ("Таблица символ шифрования:")
        l = code_2.keys()
        l = list(l)
            #        сортировка кодов
        l.sort()
                #        для всех кодов сделаем красивый вывод на экран
        for i in l:
            print(i,'-', code_2[i], end = '  \n')
#       выходное сообщение будем писать сюда
        outmess = ''
        for i in mess:
#            вычислем сообщение по формуле
            outmess += str(pow(i[0], p-1-x) * i[1] % p)
#        выведем сообщение в числовой форме
        print("p="+str(p))
        print("g="+str(g))
        print("x="+str(x))
        print("y="+str(y))
        print (outmess)
#        теперь финал. В буквенный вид
        finalOut = ''
        for i in range(0, len(outmess), 2):
#            смотрим по таблице шифрования что к чему
            tmp = int(outmess[i:i+2])
#            добавляем буквы в строку
            finalOut += code_2[tmp]
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
f = open('message.txt', 'r')
mess = f.readline()
f.close()
Main(mess)


