import requests as rq
from bs4 import BeautifulSoup as bs

#no funciona con pagina de busqueda pero si en catalogo.
#pagina = rq.get('https://simple.ripley.cl/search/redmi%20note%209?sort=score&page=1&s=o')

pagina = rq.get('https://simple.ripley.cl/tecno/telefonia/xiaomi')

soup = bs(pagina.text, 'lxml')
lista_producto = soup.find_all('a', class_="catalog-product-item")

for elem in lista_producto:
    marca = elem.find('div', class_='brand-logo')
    nombre = elem.find('div', class_='catalog-product-details__name')
    precio = elem.find('li', class_='catalog-prices__offer-price')
    #print(marca,' ---   ', nombre,' ----  ', precio)
    if None in (marca, nombre, precio):
        print('no hay datos!')
        continue
    print(marca.text.strip())
    print(nombre.text.strip())
    print(precio.text.strip(),"\n")
