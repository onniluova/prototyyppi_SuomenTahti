from geopy import distance
import random
def etäisyysLasku(nykyinen, kohde):
    nykyinenSijainti = (nykyinen.longitude, nykyinen.latitude)
    kohdeSijainti = (kohde.longitude, kohde.latitude)
    etäisyys = distance.distance(nykyinenSijainti, kohdeSijainti).km * 0.3
    return etäisyys

def polttoaineLaskuri(etäisyys, polttoaine):
    return etäisyys <= polttoaine

def polttoaineenVähennys(nykyinenPolttoaine, etäisyys):
    # Lasketaan polttoaineen kulutus sääolosuhteiden mukaan.
    sää = random.randint(0, 2)
    if sää == 0:
        kulutuskerroin = 0.90
        print("Hyvä sää. Myötätuuli avusti ja kulutit vähemmän polttoainetta.")
    elif sää == 1:
        kulutuskerroin = 1.10
        print("Huono sää. Kulutit enemmän polttoainetta.")
    else:
        kulutuskerroin = 1

    # Lasketaan polttoaineen vähennys.
    polttoaineenVähennys = etäisyys * kulutuskerroin

    # Vähennetään polttoainetta.
    nykyinenPolttoaine -= polttoaineenVähennys

    # Palautetaan polttoainemäärä.
    return round(nykyinenPolttoaine, 1)
#saa = random.randint(0, 2)

#if saa == 0:
#    polttoaine -= (polttoaineenMenetys * 0.85)
#elif saa == 1:
#    polttoaine -= (polttoaineenMenetys * 1.15)
#    ilmastopisteet += 50
#else:
#    break