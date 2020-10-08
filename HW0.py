import re

import pymorphy2
import pandas as pd
from nltk.probability import FreqDist


# открываем файл и приводим текст к нижнему регистру    
file = open('dom.txt', 'r', encoding='utf-8')  # если файл и код в одной папке
# file = open(input(), 'r', encoding='utf-8')  # если файл и код в разных папках, вводим путь 
dom_file = file.read().lower()

# удаляем знаки препинания
dom_file = re.sub(r'[^\w\s]','',dom_file)
dom_file = dom_file.split() # тк дальше нужен список

# создаем частотный словарь
freq_dom = FreqDist(dom_file)

# сортируем частотный словарь и записываем его в csv
df = pd.DataFrame.from_dict(freq_dom, orient = 'index')
df.columns = ['частота']
df.index.name = 'слово'
df = df.sort_values(by = ['частота'], ascending = False)
df.to_csv('freq_dom.csv', encoding='utf-8')

# лемматируем текст с помощью pymorphy2
morph = pymorphy2.MorphAnalyzer()
lem_dom = ''
for word in dom_file:
    p = morph.parse(word)[0]
    lem_dom = lem_dom + ' ' + p.normal_form

# ищем леммы с двумя буквами о
list_lem_dom = lem_dom.split()
lem_two_o = ''
for x in list_lem_dom:
    y = list(x)
    num_of_o = 0
    for z in y:
        if z == 'о':
            num_of_o += 1
    if num_of_o == 2:
        lem_two_o += ' ' + x
