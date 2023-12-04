from geopy import distance
import api

def etäisyysLasku(nykyinen, kohde):
    nykyinenSijainti = (nykyinen.longitude, nykyinen.latitude)
    kohdeSijainti = (kohde.longitude, kohde.latitude)
    etäisyys = distance.distance(nykyinenSijainti, kohdeSijainti).km * 0.3
    return etäisyys
def polttoaineLaskuri(etäisyys, polttoaine):
    return etäisyys <= polttoaine
def polttoaineenVähennys(nykyinenPolttoaine, etäisyys, kohde):
    # Lasketaan polttoaineen kulutus sääolosuhteiden mukaan.
    sää = api.palautaSääKohteesta(kohde)
    print(sää)
    if sää == "Clear":
        kulutuskerroin = 0.90
        print("Myötätuuli avusti ja kulutit vähemmän polttoainetta.")
    elif sää == "Few clouds":
        kulutuskerroin = 1.00
        print("Pilvinen sää. Normaali kulutus.")
    elif sää == "Scattered clouds":
        kulutuskerroin = 1.00
        print("Pilvinen sää. Normaali kulutus.")
    elif sää == "Snow":
        kulutuskerroin = 1.10
        print("Luminen sää. Suurempi kulutus.")
    else:
        kulutuskerroin = 1
        print("Säätila ei vaikuta kulutukseen.")

    # Lasketaan polttoaineen vähennys.
    polttoaineenVähennys = etäisyys * kulutuskerroin

    # Vähennetään polttoainetta.
    nykyinenPolttoaine -= polttoaineenVähennys

    # Palautetaan polttoainemäärä.
    return round(nykyinenPolttoaine, 1)