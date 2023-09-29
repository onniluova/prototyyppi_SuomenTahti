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
            print(self.rahaMaara)
    #Rahojen vähentäminen
    #Rahojan saaminen
class polttoaine:
    def __init__(self, polttoaineMaara = 100):
        self.polttoaineMaara = polttoaineMaara
    #Polttaine litroissa asetus, 100 on maksimi ja tankki on täynnä alussa
    #Tankkaus funktio, tankkaamisesta tulee maksaa sitten, kun et voi liikkua enää mihinkään. Tankkaaminen maksaa 100 euroa.

class tankkaus:
    def tankki_tayteen(self, rahat, polttoaine):
        if rahat >= 100:
            polttoaine = 100
            rahat -= 100
        else:
            print("Rahat ei riitä tankin täyttämiseen. ")

        return rahat, polttoaine

rahat = 500
polttoaine = 0

rahat, polttoaine = tankki_tayteen(rahat, polttoaine)

print("Rahaa jäljellä:", rahat)
print("Polttoainetta tankissa:", polttoaine)
class sijainti:
    def __init__(self, koordinaatit):
        self.koordinaatit = koordinaatit
    #SQL koordinaattien yhdistäminen tähän.
    #Koordinaattien vertailu polttoaineen määrään kun liikutaan.
    #Etäisyyden mittaaminen Geopyllä Rovaniemeen ja paikkaan mihin liikutaan.