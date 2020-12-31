import requests as rq
from bs4 import BeautifulSoup as bs

pagina = rq.get('https://www.pcfactory.cl/smartphones?categoria=432&papa=645')

soup = bs(pagina.text, 'lxml')

lista_producto = soup.find_all('div', class_='center-caluga')

for elem in lista_producto:
    marca = elem.find('span', class_='marca')
    nombre = elem.find('span', class_='nombre')
    precio = elem.find('span', class_='txt-precio')
    if None in (marca, nombre, precio):
        print('no hay datos!')
        continue
    print(marca.text.strip())
    print(nombre.text.strip())
    print(precio.text.strip(),"\n")
