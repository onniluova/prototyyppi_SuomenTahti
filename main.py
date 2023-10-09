import Systeemi
import satunnaisetTapahtumat

#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.

rahaSys = Systeemi.rahat()
satnnuinen = satunnaisetTapahtumat.Heitto()

pelaajanNimi = input(("Tervetuloa pelaamaan Suomen Tähteä! Syötä nimi: "))
print("Hei, " + pelaajanNimi)


print(sattuma(noppa))
##
print("Rahasi: " + str(rahaSys.tarkistaRahatilanne(50)))
