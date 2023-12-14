# Johannes Tynkkynen

import numpy as np

def Laskuri():
    brutto = input("Ilmoita bruttotulot (€/kk): ")

    try:
        netto = NettoLaskuri(int(brutto))
    except:
        print("Virhe laskuissa!")

def NettoLaskuri(brutto):
    if brutto < 0:
        print("Virhe tuloissa!")
        return 
    elif brutto < 1250:
        veropros = 0.087
        netto = (1-veropros)*brutto
    else: 
        a = 0.17316796831391448
        b = -1.1298145071451213
        
        # Calculate y using the formula
        y = a * np.log(b * brutto)
        
        #veropros = 4*10**(-7)*brutto**3-0.0001*brutto**2 + 0.0096*brutto + 0.083
        netto = (1-y)*brutto
    
        print("Veroprosentti:", y)
    return netto
    
    

    


print("Tämä on...")
Laskuri()