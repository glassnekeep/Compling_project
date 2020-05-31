from nltk import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
import os
from collections import Counter
from pprint import pprint
import math
import re
import random

stopwords = stopwords.words('russian')+[a for a in punctuation]
with open("Texts/Project_COMPLING_02.txt", 'r', encoding='utf-8') as file:
    content = file.read()

tokens = word_tokenize(content)
tokens_no_sw =[]

tokens_no_sw = [token for token in tokens if token not in stopwords]

print(tokens_no_sw)

path1 = 'C:/Users/ASUS/Desktop/Project_compling/Texts/Project_COMPLING_'
fnames1 = ['02', '03', '05', '06', '09', '10', '11', '14', '21', '22', '24', '25', '27', '30', '32', '33', '35', '38', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61']
for name in fnames1:
    with open(path1 + name+'.txt', 'r', encoding='utf-8') as file:
        text1 = file.read().lower()
        tokens1 = word_tokenize(text1)
        tokens_no_sw = [token for token in tokens1 if token not in stopwords] + tokens_no_sw

path2 = 'C:/Users/ASUS/Desktop/Project_compling/Texts/Правильные тетраэдры_'
fnames2 = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41']
for name in fnames2:
    with open(path2 + name+'.txt', 'r', encoding='utf-8') as file:
        text2 = file.read().lower()
        tokens2 = word_tokenize(text2)
        tokens_no_sw = [token for token in tokens2 if token not in stopwords] + tokens_no_sw

print(tokens_no_sw, '\n')


freq = Counter(tokens_no_sw).most_common(30)
print(freq, '\n')
relative = []
for el in freq:
    word = el[0]
    fr = el[1] / (len(tokens1)+len(tokens2))
    relative.append([word, fr])
pprint(relative)

with open('Texts/СЛОВА.txt', 'w', encoding = 'utf-8') as pile:
    for tokenss in tokens_no_sw:
        pile.write(tokenss+'\n')

ploscosti: str = '1.'

for i in range(len(tokens_no_sw)):
    if (tokens_no_sw[i] == 'плоскость') or (tokens_no_sw[i] == 'плоскости') or (tokens_no_sw[i] == 'плоскостью'):
        ploscosti = ploscosti + ' ' + tokens_no_sw[i-1] + ' ' + tokens_no_sw[i+1]

print(ploscosti)


#С помощью регулярных выражений ищем названия плоскостей, отрезков, прямых и т.д.
with open('Texts/СЛОВА.txt', 'r', encoding = 'utf-8') as f:
    text1 = f.read()
    oboznacheniya = re.findall(r'[a-z][a-z]*', text1) + re.findall(r'[a-z][a-z]*', text2)

print(oboznacheniya)


#проверка моей гипотезы, может удасться её доработать и не разбивать задачу на подзадачи

zadacha = ['дан']


for i in range(len(tokens_no_sw)-1):
    dlina = len(zadacha)
    if zadacha[dlina-1] == tokens_no_sw[i]:
        list = [tokens_no_sw[i+1]]
        zadacha = zadacha + list

print(zadacha)
print('ВОТ ЗАДАЧА')


#тут будем вычленять первое предложение из каждого файла, чтобы понять, какой может быть первая фраза.

arrayOffirsts = '1'

path1 = 'C:/Users/ASUS/Desktop/Project_compling/Texts/Project_COMPLING_'
fnames1 = ['02', '03', '05', '06', '09', '10', '11', '14', '21', '22', '24', '25', '27', '30', '32', '33', '35', '38', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61']
for name in fnames1:
    # по очереди открываем файлы и извлекаем имена
    with open(path1 + name+'.txt', 'r', encoding='utf-8') as file:
        text1 = file.read().lower()
        first1 = text1.split('.')[0]
        #arrrayOffirsts = arrayOffirsts + ' ' + first1
        print(first1)

path2 = 'C:/Users/ASUS/Desktop/Project_compling/Texts/Правильные тетраэдры_'
fnames2 = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41']
for name in fnames2:
    # по очереди открываем файлы и извлекаем имена
    with open(path2 + name+'.txt', 'r', encoding='utf-8') as file:
        text2 = file.read().lower()
        first2 = text1.split('.')[0]
        #arrrayOffirsts = arrayOffirsts + '\n' + first2
        print(first2)

#print(arrayOffirsts)


#тут начинаем описание шаблонов и подготовку массивов генерируемых значений

Zadacha1 = 'Задача: Дан'

mnogogranniki = ['тетраэдр', 'куб', 'параллелепипед', 'пирамида', 'призма']
mnogogrannik1 = ' '


random1 = random.randint(0, 4)
randombin = random.randint(1, 3)
randombinarnoe = random.randint(1, 2)
mnogogrannik = mnogogranniki[random1]

vkotorom = ', в котором'

nazvanie = ' '

print(mnogogrannik)

uglovost = 'угольная '

if(randombinarnoe == 1):
    uglovost = 'тре' + uglovost
else:
    uglovost = 'четырёх' + uglovost

if(mnogogrannik == 'пирамида'):
    if(uglovost == 'тре'):
        nazvanie = ' abc'
        mnogogrannik1 = mnogogrannik + nazvanie
    else:
        nazvanie = ' abcd'
        mnogogrannik1 = mnogogrannik + nazvanie

if(mnogogrannik == 'призма'):
    if(uglovost == 'тре'):
        nazvanie = ' abca1b1c1'
        mnogogrannik1 = mnogogrannik + nazvanie
    else:
        nazvanie = ' abcda1b1c1d1'
        mnogogrannik1 = mnogogrannik + nazvanie

if (mnogogrannik == 'пирамида' or mnogogrannik == 'призма'):
    Zadacha1 = 'Дана'
    vkotorom = ', в которой'
    if(randombin == 1):
        mnogogrannik1 = ' правильная ' + uglovost + mnogogrannik1
    elif(randombin == 2):
        mnogogrannik1 = ' прямая ' + uglovost + mnogogrannik1
    else:
        mnogogrannik1 = ' ' + uglovost + mnogogrannik1

if(mnogogrannik == 'тетраэдр'):
    nazvanie = ' abcd'
    mnogogrannik1 = mnogogrannik + nazvanie

if(mnogogrannik == 'параллелепипед'):
    nazvanie = ' abcda1b1c1d1'
    mnogogrannik1 = mnogogrannik + nazvanie


if ((mnogogrannik == 'тетраэдр') or (mnogogrannik == 'параллелепипед')):
    if(randombin == 1):
        mnogogrannik1 = ' правильный ' + mnogogrannik1
    elif((randombin == 2) and (mnogogrannik == 'параллелепипед')):
        mnogogrannik1 = ' прямой ' + mnogogrannik1
    else:
        mnogogrannik1 = ' ' + mnogogrannik1

if(mnogogrannik == 'куб'):
    nazvanie = ' abcda1b1c1d1'
    mnogogrannik1 = ' ' + mnogogrannik + nazvanie

Zadacha1 = Zadacha1 + mnogogrannik1 + vkotorom

print(Zadacha1)

print(nazvanie)

letters = []

print(len(nazvanie))

random_number_1 = 0
random_number_2 = 0
random_letter_1 = 'a'
random_letter_2 = 'a'
dlina = 1

for i in range(3):
    random_number_1 = random.randint(1, len(nazvanie)-1)
    print(random_number_1)
    random_number_2 = random.randint(1, len(nazvanie)-1)
    print(random_number_2)
    if(random_number_1 == random_number_2):
        random_number_1 = random_number_1 + 1
    random_letter_1 = nazvanie[random_number_1]
    print(random_letter_1)
    random_letter_2 = nazvanie[random_number_2]
    print(random_letter_2)
    if(random_letter_1 == '1'):
        random_letter_1 = nazvanie[random_number_1 - 1] + random_letter_1
    if(random_letter_2 == '1'):
        random_letter_2 = nazvanie[random_number_2 - 1] + random_letter_2
    print(random_letter_1)
    print(random_letter_2)
    dlina = random.randint(1, 20)
    Zadacha1 = Zadacha1 + ' ' + random_letter_1 + random_letter_2 + '=' + str(dlina) + ','

print(Zadacha1)

tochki_deleniya = ['x', 'm', 'n', 'p', 'q', 'r', 's', 'k', 'h', 'y']
random_tochka_number = 0
random_tochka = 'n'

Zadacha1 = Zadacha1 + ' причём '

randomnoe_otnoshenie1 = random.randint(1, 10)
randomnoe_otnoshenie2 = random.randint(1, 10)
spisok_tochek = [0]*3

for i in range(3):
    random_tochka_number = random.randint(2, len(tochki_deleniya) - 1)
    random_tochka = tochki_deleniya[random_tochka_number]
    for j in range(3):
        if spisok_tochek[j] == random_tochka:
            random_tochka = tochki_deleniya[random_tochka_number - 1]
    spisok_tochek[i] = random_tochka
    random_number_1 = random.randint(1, len(nazvanie)-1)
    print(random_number_1)
    random_number_2 = random.randint(1, len(nazvanie)-1)
    print(random_number_2)
    random_letter_1 = nazvanie[random_number_1]
    print(random_letter_1)
    random_letter_2 = nazvanie[random_number_2]
    print(random_letter_2)
    if(random_letter_1 == random_letter_2):
        if(random_number_2) == 1:
            random_letter_2 = nazvanie[random_number_2 + 1]
        else:
            random_letter_2 = nazvanie[random_number_2 - 1]
    if(random_letter_1 == '1'):
        random_letter_1 = nazvanie[random_number_1 - 1] + random_letter_1
    if(random_letter_2 == '1'):
        random_letter_2 = nazvanie[random_number_2 - 1] + random_letter_2
    if(random_letter_1 == random_letter_2):
        if(random_number_2) == 1:
            random_letter_2 = nazvanie[random_number_2 + 1]
        else:
            random_letter_2 = nazvanie[random_number_2 - 1]
    print(random_letter_1)
    print(random_letter_2)
    randomnoe_otnoshenie1 = random.randint(1, 10)
    randomnoe_otnoshenie2 = random.randint(1, 10)
    Zadacha1 = Zadacha1 + random_tochka + ' принадлежит ' + random_letter_1 + random_letter_2 + ' и делит этот отрезок в отношении ' + str(randomnoe_otnoshenie1) + ' : ' + str(randomnoe_otnoshenie2) + ', '

print(Zadacha1)

print(spisok_tochek)

ploskost_zadanie = ''

for i in range(3):
    ploskost_zadanie = ploskost_zadanie + spisok_tochek[i]

print(ploskost_zadanie)

volume = ''

if(len(nazvanie) == 5):
    volume = nazvanie[4]
else:
    for i in range(5, 13):
        volume = volume + nazvanie[i]

print(volume)

Vopros_zadachi1 = ' постройте сечение ' + nazvanie + ' плоскостью ' + ploskost_zadanie + '.'
Vopros_zadachi2 = ' найдите отношение объёмов ' + nazvanie + ' и ' + ploskost_zadanie + volume + '.'

Vopros_zadachi = Vopros_zadachi1

randombinarnoe = random.randint(1, 2)

if(randombinarnoe == 2):
    Vopros_zadachi = Vopros_zadachi2

Zadacha1 = Zadacha1 + Vopros_zadachi

print(Zadacha1)