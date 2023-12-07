
#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.
import lentoasemat
import etäisyys
import siirryKohteeseen
import nopanHeittoFunktio
class Peli:
    peliLoppu = 0
    rahat = 500
    polttoaine = 100
    ilmastopisteet = 100
    kilometrit = 0
    # laittakaa alustukset konstruktoriin niin on selkeää mitä objektin luonnissa tapahtuu

    def haeKentät(self):
        lentoasema_lista = lentoasemat.kohteet()
        nykyinenSijainti = lentoasema_lista["EFMA"]
        mahdollisetKohteet = []
        return lentoasema_lista, nykyinenSijainti, mahdollisetKohteet

    def siirryKohteeseen(self):
        self.polttoaine, self.nykyinenSijainti, self.kilometrit, self.lentoasema_lista = siirryKohteeseen.siirryKohteesesen(self.polttoaine, self.kilometrit, self.nykyinenSijainti, self.lentoasema_lista)
        self.mahdollisetKohteet.clear() # Tyhjennetään lista.
        self.ilmastopisteet -= 10
        print("Kohteesi: " + self.nykyinenSijainti.nimi)
        return self.polttoaine, self.nykyinenSijainti, self.kilometrit, self.lentoasema_lista

    if polttoaine <= 0:
        print("Polttoaine loppui ja koneesi tippui. Hävisit pelin.")
        exit()

    def heitaNoppaa(self):
        noppa = nopanHeittoFunktio.Noppa()
        self.rahat, self.ilmastopisteet, self.polttoaine = noppa.nopanHeitto(self.rahat, self.ilmastopisteet, self.polttoaine)

    if rahat >= 100 - polttoaine:
        määrä = (100 - polttoaine)
        rahat -= 100 - polttoaine
        round(rahat)
        polttoaine = 100
        ilmastopisteet -= 10
        print("Tankkasit " + str(määrä) + " litraa." + " Menetit 10 ilmastopistettä.")

    print("Hei hei!")
    peliLoppu = 1

    print("Virheellinen syöte!")