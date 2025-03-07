
#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.
import lentoasemat
import etäisyys
import siirryKohteeseen
import nopanHeittoFunktio
import etsiMahdollisetKohteet
import api
class Peli:
    def __init__(self, message = "", peliLoppu = 0, rahat = 500, polttoaine = 100, ilmastopisteet = 100, kilometrit = 0, lentoasema_lista = [], mahdollisetKohteet = [], nykyinenSijainti = []):
        self.peliLoppu = peliLoppu
        self.rahat = rahat
        self.polttoaine = polttoaine
        self.ilmastopisteet = ilmastopisteet
        self.kilometrit = kilometrit
        self.nykyinenSijainti = lentoasemat.kohteet()['EFMA']
        self.lentoasema_lista = lentoasemat.kohteet()
        self.mahdollisetKohteet = []
        self.message = message
    # laittakaa alustukset konstruktoriin niin on selkeää mitä objektin luonnissa tapahtuu testi

    def palautaSäänTiedot(self, airport_id):
        self.sää = api.palautaKaikkiSääKohteesta(self.lentoasema_lista[airport_id].municipality)
        return self.sää

    def haeKentät(self):
        self.lentoasema_lista = lentoasemat.kohteet()
        return self.lentoasema_lista

    def haeMahdollisetKentät(self):
        self.mahdollisetKohteet = etsiMahdollisetKohteet.etsiMahdollisetKohteet(self.nykyinenSijainti, self.polttoaine, self.lentoasema_lista)
        return self.mahdollisetKohteet

    def siirryKohteeseen(self, airport_id):
        self.polttoaine, self.nykyinenSijainti, self.kilometrit, self.lentoasema_lista = siirryKohteeseen.siirryKohteesesen(self.polttoaine, self.kilometrit, self.nykyinenSijainti, self.lentoasema_lista, airport_id)
        self.mahdollisetKohteet.clear() # Tyhjennetään lista.
        self.ilmastopisteet -= 10
        return self.polttoaine, self.nykyinenSijainti, self.kilometrit, self.lentoasema_lista

    def heitaNoppaa(self):
        noppa = nopanHeittoFunktio.Noppa()
        message = ""
        self.rahat, self.ilmastopisteet, self.polttoaine, self.message = noppa.nopanHeitto(self.rahat, self.ilmastopisteet, self.polttoaine, self.message)
        return self.rahat, self.ilmastopisteet, self.polttoaine, self.message

    def tankkaus(self):
        if (self.rahat >= 100 - self.polttoaine):
            self.rahat -= 100 - self.polttoaine
            round(self.rahat)
            self.polttoaine = 100
            self.ilmastopisteet -= 10
            return self.rahat, self.polttoaine, self.ilmastopisteet