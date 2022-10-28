import bs4
import requests
import regex

"""CLASSE CHE RACCHIUDE LE CARATTERISTICHE DI UN PRODOTTO"""
class Prodotto:
    def __init__(self, categoria, marca, descrizione, prezzo, link,display, ram, processore, memoria):
        self.categoria = categoria
        self.marca = marca
        self.descrizione = descrizione
        self.prezzo = prezzo
        self.link = link
        self.display = display
        self.memoria = ram
        self.processore = processore
        self.memoria = memoria

class prodotto:
    def __init__(self, categoria, marca, descrizione, prezzo, link, processore,display, memoria ):
        pass


"""FUNZIONE UTILE PER ESTRARRE LA MARCA CHE E' LA PRIMA PAROLA DELLA DESCRIZIONE"""
def estrai_sottostringa(Stringa):
    ind = Stringa.find(" ")
    stringa = Stringa[0:ind]
    return stringa


def Mediaword_link(Link):
    pre_link = "https://www.mediaworld.it"
    response = requests.get(Link)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    div_prodotto = soup.find('div', class_='StyledBox-sc-1vld6r2-0 goTwsP StyledFlexBox-sc-7l2z3t-1 ljqTAF')
    a_prodotti = div_prodotto.find_all('a')
    links = []

    for a_prodotto in a_prodotti:
        half_link_prodotto = str(a_prodotto.get('href'))  # con get estrapolo il link href dall'hiperlink
        link_prodotto = pre_link + half_link_prodotto

        links.append(link_prodotto)
    return links

def Unieuro(Link):
    pre_link = "https://www.unieuro.it/"
    response = requests.get(Link)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    div_prodotto = soup.find('div', class_='items-container listing__items items-section')
    a_prodotti = div_prodotto.find_all('a')
    links = []

    for a_prodotto in a_prodotti:
        half_link_prodotto = str(a_prodotto.get('href'))
        link_prodotto = pre_link+half_link_prodotto

        links.append(link_prodotto)
    return links
"""FUNZIONE PER ACQUISIRE I CAMPI DI INTERESSE DI UN PRODOTTO MEDIAWORD"""
def AttributiMediaword(link):
    response = requests.get(link)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    div_descr = soup.find('div', class_='StyledFallbackDescription-p34060-0 blRerf')
    descr = div_descr.getText()
    descr = str(descr)

    marca = estrai_sottostringa(descr)

    div_prezzo = soup.find('span', class_ ='ScreenreaderTextSpan-sc-11hj9ix-0 kZCfsu')
    x = div_prezzo.getText()
    x = x.replace('undefined ','')
    prezzo = x

    div_display = soup.findAll('td', text = " .* pollici")
    #div_display = div_display_.findall('td', class_ ='StyledDataCell-y8xttg-0 izdyJt StyledTableCell-ea56b7-2 jCWWgG')

    display = div_display[0].getText()



    return marca , prezzo, link, descr, display


"""**********************************************************************************"""
link_list = ["https://www.mediaworld.it/it/category/notebook-200101.html?page="] #, "https://www.mediaworld.it/it/search.html?page=5&query=smartphone",
    # "https://www.mediaworld.it/it/search.html?query=tablet&t=1666774334565"]
#link_list2 = ["https://www.euronics.it/informatica/computer-portatili/"]


"""
for l in link_list:
    links = Mediaword_link(l)
    for link in links:
        print(attributi(link))
        #print(link)
"""
Link = Unieuro("https://www.unieuro.it/online/?q=notebook&gclsrc[0]=aw.ds&gclsrc[1]=aw.ds&dstid=43700053003976234&adid=484314822661&gclid=Cj0KCQjw--2aBhD5ARIsALiRlwDrrGgocMzjHEnRl1KxLDoipKW4qUgf28tR5yVTxtGv9sgRM6I9e14aAoJyEALw_wcB")
for link in Link:
    print(link)


