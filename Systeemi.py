import math
class pisteet:
    def __init__(self, ilmastopisteet = 1000):
        self.ilmastopisteet = ilmastopisteet
    #Pisteiden menetys kun liikkuu
    #Pisteiden kontrollointi
class rahat:
    def __init__(self, rahaMaara = 500):
        self.rahaMaara = rahaMaara
    def tarkistaRahatilanne(self, raha):
        if self.rahaMaara >= raha:
            return(self.rahaMaara)
    #Rahojen vähentäminen
    #Rahojan saaminen
class polttoaine:
    def __init__(self, polttoaineMaara = 100):
        self.polttoaineMaara = polttoaineMaara
    #Polttaine litroissa asetus, 100 on maksimi ja tankki on täynnä alussa
    #Tankkaus funktio, tankkaamisesta tulee maksaa sitten, kun et voi liikkua enää mihinkään. Tankkaaminen maksaa 100 euroa.
    def tankki_tayteen(self, rahat, polttoaineMaara):
        if rahat.rahaMaara >= 100:
            rahat.rahaMaara -= polttoaineMaara
            polttoaineMaara = 100
        else:
            print("Rahat ei riitä tankin täyttämiseen. ")
        return rahat.rahaMaara, polttoaineMaara
def poltraha():
    print("Rahaa jäljellä:", rahat)
    print("Polttoainetta tankissa:", polttoaine)

def polttoaineen_Kulutus(self, sää):
    if sää == "hyvä":
        return self.polttoaineMaara * 0.85
    elif sää == "huono":
        return self.polttoaineMaara * 1.15
    else:
        return self.polttoaineMaara

print(polttoaineen_Kulutus("hyvä"))
print(polttoaineen_Kulutus("huono"))
print(polttoaineen_Kulutus("neutraali"))
class sijainti:
    def __init__(self, koordinaatit):
        self.koordinaatit = koordinaatit
    #SQL koordinaattien yhdistäminen tähän.
    #Koordinaattien vertailu polttoaineen määrään kun liikutaan.
    #Etäisyyden mittaaminen Geopyllä Rovaniemeen ja paikkaan mihin liikutaan.



