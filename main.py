#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.
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
        #Nopan heitto ja tapahtuma

    elif valinta == 2:
        print("Avaa kartan.")

    elif valinta == 4:
        print("Hei hei!")
        peliLoppu = 1