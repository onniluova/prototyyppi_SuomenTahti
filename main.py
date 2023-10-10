#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.
import random

peliLoppu = 0
rahat = 500
polttoaine = 100
ilmastopisteet = 0
sijainti = ""

pelaajanNimi = input(("Tervetuloa pelaamaan Suomen Tähteä! Syötä nimi: "))
print("Hei, " + pelaajanNimi)

while peliLoppu == 0:
    print("Rahamäärä:" + str(rahat))
    print("Polttoaineesi " + str(polttoaine))
    print("Sijaintisi:" + sijainti)
    valinta = int(input("Mitä haluat tehdä? 1) Liiku 2) Tankkaa 3) Kartta 4) Poistu pelistä "))

    if valinta == 1:
        print("Valitse lentokenttä: ")
        #Tähän pitää lisätä valittavat lentokentät sql tiedostosta.
        #Polttoaineen kulutus sään ja sijainnin etäisyyden mukaan.
        print("Kohteesi: " + sijainti)
        polttoaineenMenetys = int()

        #Säätilan vaikutus polttoaineeseen
        saa = random.randint(0, 2)

        if saa == 0:
            polttoaine -= (polttoaineenMenetys * 0.85)
        elif saa == 1:
            polttoaine -= (polttoaineenMenetys * 1.15)
        else:
            break

        print("Polttoaine loppui ja koneesi tippui. Hävisit pelin.")

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
        print("Avaa kartan.")

    elif valinta == 4:
        print("Hei hei!")
        peliLoppu = 1