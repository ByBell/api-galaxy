# Importer les librairies pour le scrapping
import requests as rq
from bs4 import BeautifulSoup as bs

# Charger la page que l'on veyt scrapper
r = rq.get('https://fr.wikibooks.org/wiki/Mini-guide_du_catalogue_Messier/Galaxies')

soup = bs(r.content, 'html5lib')

tables = soup.find_all('table', class_='noprint')

data = []
for table in tables:
    trs = table.find_all('tr')
    row = dict()
    for tr in trs:
        try:
            row[tr.td.get_text().strip()] = tr.td.next_sibling.next_sibling.get_text().strip()
        except AttributeError:
            pass
    data.append(row)

    row = dict()

    trs = soup.find('b', text='Type').parent.parent.parent.find_all('tr')