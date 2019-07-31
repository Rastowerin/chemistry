import urllib.request
import codecs
import json
from bs4 import BeautifulSoup


def save(data, file_name):
    with codecs.open(file_name + ".txt", "w", "utf-8-sig") as file:
        file.write(data)
        file.close()


def open(file_name):
    with codecs.open(file_name + ".txt", "r", "utf-8-sig") as json_data:
        data = json.load(json_data)
        return data


r = urllib.request.urlopen('http://www.sev-chem.narod.ru/spravochnik/rastvor.htm')
soup = BeautifulSoup(r.read(), features = "lxml")

result = soup.find_all('tr')
table = []

for x in result:
    values = x.find_all('b')
    table.append([])
    for y in values:
        element = y.text
        if len(y.text) != 1:
            if y.text[-1] in ['+', '-', '–']:
                try:
                    int(y.text[-2])
                    element = [y.text[:-2], y.text[-2:]]
                except:
                    element = [y.text[:-1], y.text[-1:]]
                if len(element[0]) != 1:
                    for z in element[0][1:]:
                        try:
                            int(z)
                        except ValueError:
                            split1 = element[0].split(element[0][1:][element[0][1:].index(z)])[0]
                            split2 = element[0].split(element[0][1:][element[0][1:].index(z)])[1]
                            element[0] = split1 + element[0][1:][element[0][1:].index(z)].lower() + split2
        table[result.index(x)].append(element)

save(str(table), 'table')


r = urllib.request.urlopen('https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%BC%D0%B5%D1%82%D0%B0%D0%BB%D0%BB%D1%8B')
soup = BeautifulSoup(r.read(), features="lxml")

result = soup.find('tbody').find_all('a')
non_metals = []

for x in result:
    non_metals.append(x.text)


r = urllib.request.urlopen('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%85%D0%B8%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D1%85_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2')
soup = BeautifulSoup(r.read(), features="lxml")
all_elements = []

result = soup.find_all('table')[1].find_all('tr')

for x in result:
    if result.index(x) != 0:
        all_elements.append(x.find_all('td')[2].text)

save(str(all_elements), 'all_elements')


r = urllib.request.urlopen('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D0%B5%D0%B9_%D0%BE%D0%BA%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2')
soup = BeautifulSoup(r.read(), features="lxml")

result = soup.find('tbody').find_all('tr')

result1 = []
result2 = []
valence = {}

for x in result:
    for y in x.find_all('td'):
        result1.append(y.text)

for x in result1:
    if x.isalpha():
        result2.append(x)
    for y in ['+', '-', '−']:
        if y in x:
            result2.append(x)

for x in result2:
    element_valence = []
    if x.isalpha():
        y = 1
        while not result2[result2.index(x) - y].isalpha():
            if result2[result2.index(x) - y][0] in ['-', '−']:
                if int(result2[result2.index(x) - y][1]) not in element_valence:
                    element_valence.append(int(result2[result2.index(x) - y][1]))
            y += 1

        try:
            y = 1
            while not result2[result2.index(x) + y].isalpha():
                if result2[result2.index(x) + y][0] == '+':
                    if int(result2[result2.index(x) + y][1]) not in element_valence:
                        element_valence.append(int(result2[result2.index(x) + y][1]))
                y += 1
        except IndexError:
            None

        valence[x] = element_valence

save(str(valence), 'valence')


def restrictions(valence):
    for x in valence.keys():
        if x == 'O':
            valence[x] = [2]
        elif x == 'Fe':
            valence[x] = [2, 3]


restrictions(valence)

