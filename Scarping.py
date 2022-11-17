import bs4
import requests
import os
import shutil

"""METODO PER ESTRARRE LA PRIMA PAROLA DA UNA STRINGA"""
def SottoStringa(s):
    ind = s.find(" ")
    stringa = s[0:ind]
    return stringa


"""METODO CHE SOSTITUISCE L'ULTIMO CARATTERE DI UNA STRINGA """
def SostituisciCarattere(stringa,i):
    max = len(stringa)
    stringa = stringa[0:max-1]
    stringa = stringa+str(i)
    return stringa


"""METODO CHE CONTROLLA CHE TUTTI GLI ATTRIBUTI DI INTERESSE
    SIANO STATI ESTRATTI CORRETTAMENTE"""
def CheckAttribti (marca, prezzo, link, descr ):
    return marca and prezzo and link and descr


"""METODO CHE CONTROLLA CHE CI SIA LA DIRECTORY PER SALVARRE I FILE
    SE NON ESISTE LA CREA"""
def CheckDir():
    curr = str(os.getcwd()+'\File_scraping')
    try:
        namesDest= os.listdir(curr)
    except:
        os.makedirs(curr)


"""METODO CHE ESTRAE TUTTI GLI HIPERLINK DAL SITO MEDIAWORD"""
def Mediaword_link(Link, link_list):
    pre_link = "https://www.mediaworld.it"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    response = requests.get(Link,headers =headers  )
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    div_prodotto = soup.find('div', class_='StyledBox-sc-1vld6r2-0 goTwsP StyledFlexBox-sc-7l2z3t-1 ljqTAF')
    a_prodotti = div_prodotto.find_all('a')

    for a_prodotto in a_prodotti:
        half_link_prodotto = str(a_prodotto.get('href'))  # con get estrapolo il link href dall'hiperlink
        link_prodotto = pre_link + half_link_prodotto

        link_list.append(link_prodotto)


"""METODO CHE DATO UN LINK DI DI UNA PAGINA MEDIAWORD
    ESTRAE I CAMPI DI INTERESSE"""
def AttributiMediaword(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(link, headers=headers)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    div_descr = soup.find('div', class_='StyledFallbackDescription-p34060-0 blRerf')
    descr = div_descr.getText()
    descr = str(descr)

    marca = SottoStringa(descr)

    div_prezzo = soup.find('span', class_ ='ScreenreaderTextSpan-sc-11hj9ix-0 kZCfsu')

    x = div_prezzo.getText()
    x = x.replace('undefined ','')
    prezzo = x

    #div_display = soup.find('td', class_='StyledDataCell-y8xttg-0 izdyJt StyledTableCell-ea56b7-2 jCWWgG')
    #display = div_display.getText()

    #div_processore = soup.find('td', class_='StyledDataCell-y8xttg-0 izdyJt StyledTableCell-ea56b7-2 jCWWgG')

    return marca , prezzo, link, descr



#---------------------------------------------------------------------------#
#       DA QUI PARTONO LE ISTRUZIONI DEL PROGRAMMA VERO E PROPRIO
#---------------------------------------------------------------------------#
link_notebook = 'https://www.mediaworld.it/it/category/notebook-200101.html?page=1'
link_smartphone = 'https://www.mediaworld.it/it/search.html?query=smartphone&page=1'
link_tablet = 'https://www.mediaworld.it/it/search.html?query=tablet&page=1'

link_list_notebook = []
link_list_smartphone = []
link_list_tablet = []
link_list = []

for i in range (1,8):
    Mediaword_link(SostituisciCarattere(link_notebook,i),link_list_notebook)
    Mediaword_link(SostituisciCarattere(link_smartphone,i),link_list_smartphone)
    Mediaword_link(SostituisciCarattere(link_tablet,i),link_list_tablet)
link_list.extend(link_list_notebook)
link_list.extend(link_list_smartphone)
link_list.extend(link_list_tablet)




for link in link_list:
    marca,prezzo, links, descrizione = AttributiMediaword(link)
    CheckDir()
    # CAMBIARE LA DIRECTORY DA QUELLA ATTUALE A QUELLA DEI FILE
    if (CheckAttribti(marca, prezzo, link, descrizione)):
        """TO DO creo un file in scrittura, ci scrivo dentro tutti gli attributi
            e lo chiudo"""
        print(prezzo, links)
        #print(marca, prezzo, link, descrizione)