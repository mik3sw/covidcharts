import functions
from functions import regioni as r
        
print('= Menù Regioni =')
print('1: Abruzzo                       12: P.A. Bolzano\n'
      '2: Basilicata                    13: P.A. Trento\n'
      '3: Calabria                      14: Piemonte\n'
      '4: Campania                      15: Puglia\n'
      '5: Emilia-Romagna                16: Sardegna\n'
      '6: Friuli Venezia Giulia         17: Sicilia\n'
      '7: Lazio                         18: Toscana\n'
      '8: Liguria                       19: Umbria\n'
      '9: Lombardia                     20: Valle d\'Aosta\n'
      '10: Marche                       21: Veneto\n'
      '11: Molise\n')
print("Inserire il numero della regione: ")

def setreg(reg):
    if int(reg)>0 and int(reg)<22:
        regione = r[int(reg)]
        data = functions.start()
        functions.dograph(data, regione)
    else:
        print('Input non corretto')

reg = input()
setreg(reg)