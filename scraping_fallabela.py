import requests as rq
from bs4 import BeautifulSoup as bs

pagina = rq.get('https://www.falabella.com/falabella-cl/search?Ntt=redmi+note+9')
#pagina = rq.get('https://www.falabella.com/falabella-cl/search?Ntt=piscina+intex')

soup = bs(pagina.text, 'lxml')

lista_producto = soup.find_all('div', class_="jsx-1585533350")

productos = []
for elem in lista_producto:
    marca = elem.find('b', class_='pod-title')
    nombre = elem.find('b', class_='pod-subTitle')
    precio = elem.find('li', class_='price-0')
    #rint(marca,' - ', nombre,' - ', precio)
    if None in (marca, nombre, precio):
        print('no hay datos!')
        continue
    marca = marca.text.strip()
    nombre = nombre.text.strip()
    precio = precio.text.strip()
    tupla = (marca, nombre, precio)
    productos.append(tupla)

falabella = {'falabella': productos}
print(falabella)