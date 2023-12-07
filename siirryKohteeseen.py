import lentoasemat
import etäisyys
def siirryKohteesesen(polttoaine, kilometrit, nykyinenSijainti, lentoasema_lista):

    # Eritellään mahdollisetkohteet funktio ja siirryKohteeseen funktio.

    mahdollisetKohteet = []

    for key in lentoasema_lista:  # Looppi käy läpi lentoasema sanakirjan ja lisää tiedot kenttä muuttujaan.
        kenttä = lentoasema_lista[key]
        etäisyydet = etäisyys.etäisyysLasku(nykyinenSijainti, kenttä)  # Luodaan etäisyyden mittaamisesta muuttuja. Otetaan funktio etäisyydet tiedostosta.
        if etäisyys.polttoaineLaskuri(etäisyydet, polttoaine) == True:  # Jos funktio palauttaa true, lisätään kenttä mahdollisiin kohteisiin.
            mahdollisetKohteet.append(kenttä)
    # Printataan nimet ja icao koodit
    for t in mahdollisetKohteet:
        etäisyydet1 = etäisyys.etäisyysLasku(nykyinenSijainti, t)
        # print(t.nimi + " " + t.id + " " + str(etäisyydet1) + " km")
        print(f"{t.nimi} {t.id}. Etäisyys lentokentälle: {etäisyydet1:.1f} km")

    lentokentta = input("Valitse lentokenttä: ")

    for key in lentoasema_lista:
        if lentoasema_lista[key].id == lentokentta:
            kilometrit += etäisyys.etäisyysLasku(nykyinenSijainti, lentoasema_lista[key]) * 4
            etäisyysVälillä = etäisyys.etäisyysLasku(nykyinenSijainti, lentoasema_lista[key])  # Tehdään muuttuja etäisyydestä.
            polttoaine = etäisyys.polttoaineenVähennys(polttoaine, etäisyysVälillä, lentoasema_lista[key].municipality)  # Vähennetään polttoainetta
            nykyinenSijainti = lentoasema_lista[key]  # Muutetaan kohdesijainti nykyiseksi sijainniksi.
    mahdollisetKohteet.clear()  # Tyhjennetään lista.

    return polttoaine, nykyinenSijainti, kilometrit, lentoasema_lista