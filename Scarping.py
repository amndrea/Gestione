import bs4
import requests

"""CLASSE CHE RACCHIUDE LE CARATTERISTICHE DI UN PRODOTTO"""
class Prodotto:
    def __init__(self, categoria, marca, descrizione, prezzo, link,display):
        self.categoria = categoria
        self.marca = marca
        self.descrizione = descrizione
        self.prezzo = prezzo
        self.link = link
        self.display = display

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

    div_notebook = soup.find('div', class_='StyledBox-sc-1vld6r2-0 goTwsP StyledFlexBox-sc-7l2z3t-1 ljqTAF')
    a_notebooks = div_notebook.find_all('a')
    links = []

    for a_notebook in a_notebooks:
        half_link_pc = str(a_notebook.get('href'))  # con get estrapolo il link href dall'hiperlink
        link_pc = pre_link + half_link_pc

        links.append(link_pc)
    return links


"""FUNZIONE PER ACQUISIRE I CAMPI DI INTERESSE DI UN NOTEBOOK MEDIAWORD"""
def attributi(link):
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

    return marca , prezzo, link, descr



"""**********************************************************************************"""
link_list = ["https://www.mediaworld.it/it/category/notebook-200101.html?page=", "https://www.mediaworld.it/it/search.html?page=5&query=smartphone",
     "https://www.mediaworld.it/it/search.html?query=tablet&t=1666774334565"]

for l in link_list:
    links = Mediaword_link(l)
    for link in links:
        print(link)



