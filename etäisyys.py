from geopy import distance
import random
def etäisyysLasku(nykyinen, kohde):
    nykyinenSijainti = (nykyinen.longitude, nykyinen.latitude)
    kohdeSijainti = (kohde.longitude, kohde.latitude)
    etäisyys = distance.distance(nykyinenSijainti, kohdeSijainti).km
    return etäisyys

def polttoaineLaskuri(etäisyys, polttoaine):
    return etäisyys <= polttoaine

def polttoaineenVähennys(etäisyys, nykyinenPolttoaine):
    sää = random.randint(0, 2)
    if sää == 0:
        nykyinenPolttoaine -= (etäisyys - nykyinenPolttoaine)
    elif sää == 1:
        nykyinenPolttoaine -= (etäisyys - nykyinenPolttoaine * 0.2)
    elif sää == 2:
        nykyinenPolttoaine -= (etäisyys - nykyinenPolttoaine * 0.2)
    print(nykyinenPolttoaine)
    return nykyinenPolttoaine
#saa = random.randint(0, 2)

#if saa == 0:
#    polttoaine -= (polttoaineenMenetys * 0.85)
#elif saa == 1:
#    polttoaine -= (polttoaineenMenetys * 1.15)
#    ilmastopisteet += 50
#else:
#    break