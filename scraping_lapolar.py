import requests as rq
from bs4 import BeautifulSoup as bs

#busqueda
#pagina = rq.get('https://www.lapolar.cl/Busqueda/?q=redmi+note+9&lang=es_CL')

#catálogo
pagina = rq.get('https://www.lapolar.cl/tecnologia/celulares/smartphones/?prefn1=brand&prefv1=XIAOMI&srule=')

soup = bs(pagina.text, 'lxml')

lista_producto = soup.find_all('div', class_="product-tile__item")

print(len(lista_producto))

for elem in lista_producto:
    marca = elem.find('p', class_='brand-name')
    nombre = elem.find('a', class_='link')
    precio = elem.find('p', class_='internet')
    #rint(marca,' - ', nombre,' - ', precio)
    if None in (marca, nombre, precio):
        print('no hay datos!')
        continue
    print(marca.text.strip())
    print(nombre.text.strip())
    print(precio.text.strip(),"\n")
