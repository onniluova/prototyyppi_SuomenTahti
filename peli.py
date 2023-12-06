
#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.
import random
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

    pelaajanNimi = input(("Tervetuloa pelaamaan Läpi Suomen Maan! Syötä nimi: "))

    print("Hei, " + pelaajanNimi)

    lentoasema_lista = lentoasemat.kohteet()

    nykyinenSijainti = lentoasema_lista["EFMA"]

    mahdollisetKohteet = []

    while peliLoppu == 0:
        if nykyinenSijainti.id == "EFRO":
            peliLoppu == 1
            print("Voitit pelin, " + pelaajanNimi +  "!")
            print("__  _")
            print("\ `/ |")
            print(" \__`!")
            print(" / ,' `-.__________________")
            print("'-'\_____                ◻ `-.")
            print("   <____()-=O=O=O=O=O=[]====--)")
            print("     `.___ ,-----,_______...-'")
            print("          /    .'")
            print("         /   .'")
            print("        /  .'")
            print("        `-'")
            print("Ilmastopisteet: " + str(ilmastopisteet))
            print("Kuljetut kilometrit: " + str(round(kilometrit, 1)))
            break

        if rahat <= 0:
            print("GG")
            break

        print("Rahamäärä: " + str(round(rahat)) + " euroa")
        print("Ilmastopisteet: " + str(ilmastopisteet))
        print("Polttoaineesi: " + str(polttoaine) + " litraa")
        print("Sijaintisi: " + nykyinenSijainti.nimi)

        valinta = int(input("Mitä haluat tehdä? 1) Liiku 2) Tankkaa 3) Kartta 4) Poistu pelistä "))

        if valinta == 1:
            polttoaine, nykyinenSijainti, kilometrit, lentoasema_lista = siirryKohteeseen.valinnat(polttoaine, kilometrit, nykyinenSijainti, lentoasema_lista)

            mahdollisetKohteet.clear() # Tyhjennetään lista.

            ilmastopisteet -= 10
            print("Kohteesi: " + nykyinenSijainti.nimi)

            if polttoaine <= 0:
                print("Polttoaine loppui ja koneesi tippui. Hävisit pelin.")
                exit()

            noppa = nopanHeittoFunktio.Noppa()
            rahat, ilmastopisteet, polttoaine = noppa.nopanHeitto(rahat, ilmastopisteet, polttoaine)

        elif valinta == 2:
            if rahat >= 100 - polttoaine:
                määrä = (100 - polttoaine)
                rahat -= 100 - polttoaine
                round(rahat)
                polttoaine = 100
                ilmastopisteet -= 10
                print("Tankkasit " + str(määrä) + " litraa." + " Menetit 10 ilmastopistettä.")

        elif valinta == 3:
            print("Avaa kartan.")

        elif valinta == 4:
            print("Hei hei!")
            peliLoppu = 1

        else:
            print("Virheellinen syöte!")