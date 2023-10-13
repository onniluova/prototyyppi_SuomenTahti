#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.
import random
import lentoasemat
import etäisyys

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

    print("Rahamäärä:" + str(rahat))
    print("Ilmastopisteet: " + str(ilmastopisteet))
    print("Polttoaineesi " + str(polttoaine))
    print("Sijaintisi:" + nykyinenSijainti.nimi)

    valinta = int(input("Mitä haluat tehdä? 1) Liiku 2) Tankkaa 3) Kartta 4) Poistu pelistä "))

    if valinta == 1:
        for key in lentoasema_lista:  # Looppi käy läpi lentoasema sanakirjan ja lisää tiedot kenttä muuttujaan.
            kenttä = lentoasema_lista[key]
            etäisyydet = etäisyys.etäisyysLasku(nykyinenSijainti, kenttä)  # Luodaan etäisyyden mittaamisesta muuttuja. Otetaan funktio etäisyydet tiedostosta.
            if etäisyys.polttoaineLaskuri(etäisyydet, polttoaine) == True:  # Jos funktio palauttaa true, lisätään kenttä mahdollisiin kohteisiin.
                mahdollisetKohteet.append(kenttä)
        #Printataan nimet ja icao koodit
        for t in mahdollisetKohteet:
            etäisyydet1 = etäisyys.etäisyysLasku(nykyinenSijainti, t)
            #print(t.nimi + " " + t.id + " " + str(etäisyydet1) + " km")
            print(f"{t.nimi} {t.id} {etäisyydet1:.1f} km")
        lentokentta = input("Valitse lentokenttä: ")

        for key in lentoasema_lista:
            if lentoasema_lista[key].id == lentokentta:
                kilometrit += etäisyys.etäisyysLasku(nykyinenSijainti, lentoasema_lista[key]) * 4
                etäisyysVälillä = etäisyys.etäisyysLasku(nykyinenSijainti, lentoasema_lista[key]) #Tehdään muuttuja etäisyydestä.
                polttoaine = etäisyys.polttoaineenVähennys(polttoaine, etäisyysVälillä) #Vähennetään polttoainetta
                nykyinenSijainti = lentoasema_lista[key] #Muutetaan kohdesijainti nykyiseksi sijainniksi.

        mahdollisetKohteet.clear() # Tyhjennetään lista.

        ilmastopisteet -= 10
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
            print(f"Löysit {raha_lista[raha_maara]}€")

        elif noppa ==3:
            print("Lensit ekologisesti. Sait 10 ilmastopistettä.")
            ilmastopisteet += 1

        elif noppa == 4:
            print("Sinut ryöstettiin. Menetit 100€")
            rahat -= 100

        elif noppa == 5:
            print("Lentokoneessa on vikaa. Korjaus maksaa: -100€")
            rahat -= 100

        elif noppa in range(6,11):
            polttoaine -= 0
            print("Ei tapahdu mitään")

        elif noppa == 12:
            print("ÄMPÄRIARVONTA!!")
            ilmastopisteet += 100
            rahat += 500
        #Nopan heitto ja tapahtuma

    elif valinta == 2:
        if rahat >= 100 - polttoaine:
            rahat -= 100 - polttoaine
            round(rahat, 1)
            polttoaine = 100
            ilmastopisteet -= 10
            print("Tankkisi on täytetty. Menetit 10 ilmastopistettä.")

    elif valinta == 3:
        print("Avaa kartan.")

    elif valinta == 4:
        print("Hei hei!")
        peliLoppu = 1

    else:
        print("Virheellinen syöte!")