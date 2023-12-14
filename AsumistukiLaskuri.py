# Tehty asumistuen laskemiseen
# Kaavat haettu kelan sivuilta


def Laskuri(tulot):
    kaupunki = input("Ilmoita kaupunki (T = Turku tai Tampere, H = Helsinki): ")
    
    tulot = int(tulot)
    vuokra = input("Ilmoita vuokra: ")
    vuokra = int(vuokra)
    vesiJaAuto = input("Ilmoita muut asumiskulut (vesi ja automaksu): ")
    vesiJaAuto = int(vesiJaAuto)

    helMaxMenot = 843
    tamMaxMenot = 652
    cityName = ""
    maksimiTuki = 0.0
    if kaupunki == "T":
        cityName = "Tampere/Turku"
        if vuokra > tamMaxMenot:
            maksimiTuki = 521.6
        else:
            maksimiTuki = vuokra*0.8
        
    elif kaupunki == "H":
        cityName = "Helsinki"
        if vuokra > helMaxMenot:
            maksimiTuki = 674.4
        else:
            maksimiTuki = vuokra*0.8
    else:
        print("väärä kaupungin nimi")
        return
    
    perusOmaVastuu = 0.42*(tulot-600)-(667+111*2)

    if perusOmaVastuu < 0:
        asumistuki = maksimiTuki
    else:
        asumistuki = maksimiTuki-perusOmaVastuu

    

    print("Asumistuki: ", asumistuki, "€" )
    
    yht = vuokra+vesiJaAuto-asumistuki
    yhtKes = vuokra+vesiJaAuto
    vuosi = yht*8+yhtKes*4

    return yht, vuosi, cityName

def Vastaus(vertailu):
    if vertailu == "Y":
        lasku1 = Laskuri(tulot)
        lasku2 = Laskuri(tulot)
    elif vertailu == "N":
        lasku1 = Laskuri(tulot)
    else:
        print("Väärä valinta")
        return

    print("Asumiskulut kuukaudessa (Vuokra + muut kulut - asumituki):")
    try:
        print("Vaihtoehto 1", lasku1[2], ": ", lasku1[0], "€/kk, ", lasku1[0]/2, "€/henkilö")
        print("Vaihtoehto 2", lasku2[2], ": ", lasku2[0], "€/kk, ", lasku2[0]/2, "€/henkilö")

        kkErotus = round(lasku1[0] - lasku2[0],2)
        if kkErotus < 0:
            print("Vaihtoehto 1 on halvempi ", -kkErotus, "€/kk, eli ", -kkErotus/2, "€/henkilö")
        elif kkErotus == 0:
            print("Vaihtoehdot saman hintaisia")
        else:
            print("Vaihtoehto 2 on halvempi ", kkErotus, "€/kk, eli ", kkErotus/2, "€/henkilö")

    except:
        exit

    print("Asumiskulut vuodessa (asumistuki vähennetty):")

    try:
        print("Vuodessa vaihtoehto 1 (8 tukikuukautta): ", lasku1[1], "€, ", lasku1[1]/2, "€/henkilö")
        print("Vuodessa vaihtoehto 2 (8 tukikuukautta): ", lasku2[1], "€, ", lasku2[1]/2, "€/henkilö")

        aErotus = round(lasku1[1] - lasku2[1],2)
        if aErotus < 0:
            print("Vaihtoehto 1 on halvempi ", -aErotus, "€, eli ", -aErotus/2, "€/henkilö")
        elif aErotus == 0:
            print("Vaihtoehdot saman hintaisia")
        else:
            print("Vaihtoehto 2 on halvempi ", aErotus, "€, eli ", aErotus/2, "€/henkilö")

    except:
        exit

print("Tämä on asumistukilaskuri kahdelle hengelle")
tulot = input("Ilmoita tulot: ")
vertailu = input("Vartailu? (Y/N): ")
Vastaus(vertailu)