#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.
import random
import mysql.connector
from geopy import distance
import lentoasemat
import etäisyys

peliLoppu = 0
rahat = 1000
polttoaine = 150
ilmastopisteet = 0
kilometrit = 0

pelaajanNimi = input(("Tervetuloa pelaamaan Läpi Suomen Maan! Syötä nimi: "))
print("Hei, " + pelaajanNimi)

lentoasema_lista = lentoasemat.kohteet()

nykyinenSijainti = lentoasema_lista["EFMA"]

mahdollisetKohteet = []


#polttoaine -= distance.distance(a, b).km * 0.15

#Jos lentokenttä on Rovaniemen lentokenttä, tulosta tuloksesi ja lopeta peli.

while peliLoppu == 0:
    print("Rahamäärä:" + str(rahat))
    print("Ilmastopisteet: " + str(ilmastopisteet))
    print("Polttoaineesi " + str(polttoaine))
    print("Sijaintisi:" + nykyinenSijainti.nimi)

    for key in lentoasema_lista:
        kenttä = lentoasema_lista[key]
        etäisyydet = etäisyys.etäisyysLasku(nykyinenSijainti, kenttä)

        if etäisyys.polttoaineLaskuri(etäisyydet, polttoaine) == True:
            mahdollisetKohteet.append(kenttä)

    valinta = int(input("Mitä haluat tehdä? 1) Liiku 2) Tankkaa 3) Kartta 4) Poistu pelistä "))

    if nykyinenSijainti.nimi == "Rovaniemi Airport":
        peliLoppu == 1
        print("Voitit pelin!")
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
        print("Kuljetut kilometrit: " + str(kilometrit))

    if valinta == 1:
        for t in mahdollisetKohteet:
            print(t.nimi + " " + t.id)
        lentokentta = input("Valitse lentokenttä: ")
        for key in lentoasema_lista:
            if lentoasema_lista[key].id == lentokentta:
                etäisyysVälillä = etäisyys.etäisyysLasku(nykyinenSijainti, lentoasema_lista[key])
                polttoaine = etäisyys.polttoaineenVähennys(polttoaine, etäisyysVälillä)
                nykyinenSijainti = lentoasema_lista[key]

        # Tähän pitää lisätä valittavat lentokentät sql tiedostosta.
        # Polttoaineen sijainnin etäisyyden mukaan. Ilmastopisteiden lisäys reitin ekologisuuden mukaan.
        print("Kohteesi: " + nykyinenSijainti.nimi)

        if polttoaine <= 0:
            print("Polttoaine loppui ja koneesi tippui. Hävisit pelin.")
            exit()

        #Tapahtuman arpominen
        noppa = random.randint(1, 12)

        if noppa == 1:
            print("Lentokoneessa on vikaa. Korjaus maksaa: -100€")
            rahat -= 100

        elif noppa ==2:
            raha_lista=[100,200,300]
            raha_maara = random.randint(0,2)
            rahat += raha_lista[raha_maara]
            print(f"Löysit {raha_lista[raha_maara]}€ Rahamäärä: {rahat}")

        elif noppa ==3:
            print("Myötätuuli")

        elif noppa == 4:
            print("Sinut ryöstettiin. Menetit 100€")
            rahat -= 100

        elif noppa == 5:
            print("Lentokoneessa on vikaa. Korjaus maksaa: -100€")
            rahat -= 100
            print("Rahamäärä: " + str(rahat))

        elif noppa in range(6,11):
            polttoaine -= 0
            print("Ei tapahdu mitään")

        elif noppa == 12:
            print("ÄMPÄRIARVONTA!!")
            ilmastopisteet += 100
            rahat += 500
        #Nopan heitto ja tapahtuma

    elif valinta == 2:
        if rahat >= 150 - polttoaine:
            rahat -= 150 - polttoaine
            polttoaine = 150
            print("Tankkisi on täytetty.")

    elif valinta == 3:
        print("Avaa kartan.")

    elif valinta == 4:
        print("Hei hei!")
        peliLoppu = 1

    else:
        print("Virheellinen syöte!")