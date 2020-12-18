import requests
import matplotlib.pyplot as plt

def start():
    data_url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json'
    res = requests.get(data_url)
    data = res.json()
    return data

# dati forniti già elaborati nel file json
def get_nuovi_contagi(data, regione):
    new = []
    for item in data:
        if item['denominazione_regione'] == regione:
            new.append(item['nuovi_positivi'])
    return new

# ===========
# dati grezzi
def get_nuovi_deceduti(y, regione):
    lista = []
    for item in y:
        if item['denominazione_regione'] == regione:
            lista.append(item['deceduti'])
    return lista
    
def get_nuovi_guariti(y, regione):
    lista = []
    for item in y:
        if item['denominazione_regione'] == regione:
            lista.append(item['dimessi_guariti'])
    return lista
# ===========

# Funzione per elaborare i dati grezzi
def get_final_list(lista):
    length = 0
    new = []
    for item in lista:
        if length == 0:
            new.append(lista[0])
        else:
            tmp = lista[length]- lista[length-1]
            new.append(tmp)
        length +=1
    return new

# salvo i dati e creo il grafico
def doit(data, regione):
    guariti = get_final_list(get_nuovi_guariti(data, regione))
    morti = get_final_list(get_nuovi_deceduti(data, regione))
    contagiati = get_nuovi_contagi(data, regione)
    return guariti, morti, contagiati

def dograph(data, regione):
    guariti, morti, contagiati = doit(data, regione)
    plt.plot(contagiati, label='nuovi positivi')
    plt.plot(morti, label='morti')
    plt.plot(guariti, label='guariti')
    plt.title('COVID-19 {}'.format(regione))
    plt.xlabel('Days')
    plt.ylabel('People')
    plt.legend()
    plt.show()

regioni = {1: 'Abruzzo',
           2: 'Basilicata',
           3: 'Calabria',
           4: 'Campania',
           5: 'Emilia-Romagna',
           6: 'Friuli Venezia Giulia',
           7: 'Lazio',
           8: 'Liguria',
           9: 'Lombardia',
           10: 'Marche',
           11: 'Molise',
           12: 'P.A. Bolzano',
           13: 'P.A. Trento',
           14: 'Piemonte',
           15: 'Puglia',
           16: 'Sardegna',
           17: 'Sicilia',
           18: 'Toscana',
           19: 'Umbria',
           20: 'Valle d\'Aosta',
           21: 'Veneto'}