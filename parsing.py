import urllib.request
from bs4 import BeautifulSoup

r = urllib.request.urlopen('http://www.sev-chem.narod.ru/spravochnik/rastvor.htm')
soup = BeautifulSoup(r.read(), features = "lxml")

result = soup.find_all('tr')
table = []

for x in result:
    values = x.find_all('b')
    table.append([])
    for y in values:
        table[result.index(x)].append(y.text)

#print(table)

r = urllib.request.urlopen('https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%BC%D0%B5%D1%82%D0%B0%D0%BB%D0%BB%D1%8B')
soup = BeautifulSoup(r.read(), features = "lxml")

result = soup.find('tbody').find_all('a')
non_metals = []

for x in result:
    non_metals.append(x.text)
r = urllib.request.urlopen('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%85%D0%B8%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D1%85_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2')
soup = BeautifulSoup(r.read(), features = "lxml")
all_elements = []

result = soup.find_all('table')[2].find_all('tr')

for x in result:
    if result.index(x) != 0:
        all_elements.append(x.find_all('td')[2].text)