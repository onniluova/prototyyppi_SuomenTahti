import Systeemi
import satunnaisetTapahtumat

#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.

rahaSys = Systeemi.rahat()
satnnuinen = satunnaisetTapahtumat.noppaHeitto()

pelaajanNimi = input(("Tervetuloa pelaamaan Suomen Tähteä! Syötä nimi: "))
print("Hei, " + pelaajanNimi)



print("Rahasi: " + str(rahaSys.tarkistaRahatilanne(50)))

