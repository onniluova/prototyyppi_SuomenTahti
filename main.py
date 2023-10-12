#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.
import random
import mysql.connector
from geopy import distance
import lentoasemat

peliLoppu = 0
rahat = 500
polttoaine = 100
ilmastopisteet = 0
kilometrit = 0

pelaajanNimi = input(("Tervetuloa pelaamaan Suomen Tähteä! Syötä nimi: "))
print("Hei, " + pelaajanNimi)

lentoasema_lista = lentoasemat.kohteet()
print(lentoasema_lista)

marienhamina = lentoasema_lista["EFMA"]
print(marienhamina.nimi)

nykyinenSijainti = lentoasema_lista["EFHK"]

for key in lentoasema_lista:
    kenttä = lentoasema_lista[key]
    etäisyys = distance.distance(nykyinenSijainti, kenttä.longitude).km
    print(f"{key}: {etäisyys:.2f} km")

#polttoaine -= distance.distance(a, b).km * 0.15
print(polttoaine)

#Jos lentokenttä on Rovaniemen lentokenttä, tulosta tuloksesi ja lopeta peli.

while peliLoppu == 0:
    print("Rahamäärä:" + str(rahat))
    print("Polttoaineesi " + str(polttoaine))
    print("Sijaintisi:" + sijainti)
    valinta = int(input("Mitä haluat tehdä? 1) Liiku 2) Tankkaa 3) Kartta 4) Poistu pelistä "))

    if lentokentta == "Rovaniemi":
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
        lentokentta = input("Valitse lentokenttä: ")
        #Tähän pitää lisätä valittavat lentokentät sql tiedostosta.
        #Polttoaineen sijainnin etäisyyden mukaan. Ilmastopisteiden lisäys reitin ekologisuuden mukaan.
        print("Kohteesi: " + sijainti)
        polttoaineenMenetys = int()

        #Säätilan vaikutus polttoaineeseen
        saa = random.randint(0, 2)

        if saa == 0:
            polttoaine -= (polttoaineenMenetys * 0.85)
        elif saa == 1:
            polttoaine -= (polttoaineenMenetys * 1.15)
            ilmastopisteet += 50
        else:
            break

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
            rahat += raha_maara
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
            print("Ei tapahdu mitään")

        elif noppa == 12:
            print("ÄMPÄRIARVONTA!!")
            ilmastopisteet += 100
            rahat += 500
        #Nopan heitto ja tapahtuma

    elif valinta == 2:
        if rahat <= 100 - polttoaine:
            rahat -= 100 - polttoaine
            polttoaine = 100
            print("Tankkisi on täytetty.")

    elif valinta == 3:
        print("Avaa kartan.")

    elif valinta == 4:
        print("Hei hei!")
        peliLoppu = 1