import Systeemi
import satunnaisetTapahtumat

#Peli alkaa tästä. Pelilooppiin siirrytään kun pelaaja on valmis pelaamaan.

rahaSys = Systeemi.rahat()

pelaajanNimi = input(("Tervetuloa pelaamaan Suomen Tähteä! Syötä nimi: "))
print("Hei, " + pelaajanNimi)

#Selostus pelin juonesta

while True:
    print("Valitse määränpää") #Kolme vaihtoehtoa
    print("Rahasi: " + str(rahaSys.tarkistaRahatilanne(50))) #