import bs4
import requests

"""CLASSE CHE RACCHIUDE LE CARATTERISTICHE DI UN PRODOTTO"""
class Prodotto:

    def __init__(self, marca, descrizione, prezzo, link):
        self.marca = marca
        self.descrizione = descrizione
        self.prezzo = prezzo
        self.link = link


"""FUNZIONE UTILE PER ESTRARRE LA MARCA CHE E' LA PRIMA PAROLA DELLA DESCRIZIONE"""
def estrai_sottostringa(Stringa):
    ind = Stringa.find(" ")
    stringa = Stringa[0:ind]
    return stringa

"""Metodo che scarica tutti i dati di notebook disponibili sul sito mediaword"""
def mediaword():

    link = "https://www.mediaworld.it/it/category/notebook-200101.html?page=3"
    pre_link = "https://www.mediaworld.it"


    response = requests.get(link)   # scarica la pagina e la mette in response
    response.raise_for_status()  # genera un'eccezione se la richiesta http fallisce


    soup = bs4.BeautifulSoup(response.text, 'html.parser')  # salvo il testo HTML della pagina nella variabile soup

    # con control+shift+c trovo la sezione nel quale sono contenute le cose che mi interessano
    # e copio la classe della div
    div_notebook = soup.find('div', class_='StyledBox-sc-1vld6r2-0 goTwsP StyledFlexBox-sc-7l2z3t-1 ljqTAF')

    # all'interno della div sopra copiata, continuando l'analisi della pagina, mi accorgo che
    # ci sono tutti i link degli articoli, con all'interno degli hiperlink
    a_notebooks = div_notebook.find_all('a')   # con find_all trovo tutti gli hiperlink
    links = []  # estraggo tutti gli hiperlink della div a e li inserisco in una lista nuova



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


"""-------------------------------------------------------------------------------------"""
links = mediaword()
print(len(links))
for links_ in links:
    prodotto = attributi(links_)
    print(prodotto)


