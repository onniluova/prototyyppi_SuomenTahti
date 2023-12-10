import etäisyys

def etsiMahdollisetKohteet(nykyinenSijainti, polttoaine, lentoasema_lista):
    mahdollisetKohteet = []

    if isinstance(nykyinenSijainti, str):
        nykyinenSijainti = lentoasema_lista.get(nykyinenSijainti) # Muutetaan nykyinen sijainti lentoasema objektiksi.

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

    return mahdollisetKohteet