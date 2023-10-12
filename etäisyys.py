from geopy import distance
import random
def etäisyysLasku(nykyinen, kohde):
    nykyinenSijainti = (nykyinen.longitude, nykyinen.latitude)
    kohdeSijainti = (kohde.longitude, kohde.latitude)
    etäisyys = distance.distance(nykyinenSijainti, kohdeSijainti).km
    return etäisyys

def polttoaineLaskuri(etäisyys, polttoaine):
    return etäisyys <= polttoaine


#saa = random.randint(0, 2)

#if saa == 0:
#    polttoaine -= (polttoaineenMenetys * 0.85)
#elif saa == 1:
#    polttoaine -= (polttoaineenMenetys * 1.15)
#    ilmastopisteet += 50
#else:
#    break