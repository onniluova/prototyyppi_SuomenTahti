import lentoasemat
import etäisyys
def siirryKohteesesen(polttoaine, kilometrit, nykyinenSijainti, lentoasema_lista, airport_id):

    # Eritellään mahdollisetkohteet funktio ja siirryKohteeseen funktio.
    for key in lentoasema_lista:
        if lentoasema_lista[key].id == airport_id:
            kilometrit += etäisyys.etäisyysLasku(nykyinenSijainti, lentoasema_lista[key]) * 4
            etäisyysVälillä = etäisyys.etäisyysLasku(nykyinenSijainti, lentoasema_lista[key])  # Tehdään muuttuja etäisyydestä.
            polttoaine = etäisyys.polttoaineenVähennys(polttoaine, etäisyysVälillä, lentoasema_lista[key].municipality)  # Vähennetään polttoainetta
            nykyinenSijainti = lentoasema_lista[key]  # Muutetaan kohdesijainti nykyiseksi sijainniksi.

    return polttoaine, nykyinenSijainti, kilometrit, lentoasema_lista