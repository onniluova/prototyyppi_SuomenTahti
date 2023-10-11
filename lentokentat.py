import mysql.connector
from geopy import distance
def kohteet():
    sql = "SELECT airport.name, municipality, latitude_deg, longitude_deg, airport.ident FROM airport"
    sql += " inner join country on country.iso_country = airport.iso_country where country.name =" + "'Finland'" + " AND type = 'medium_airport'"
    sql += " order by latitude_deg"
    sql += " LIMIT 26"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        print(rivi)
    return

yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'Nasslingmaga98',
    autocommit = True
)

sijainti = "EFHK"
kohteet()

def icaokoodi(idd):
    sql = "SELECT latitude_deg, longitude_deg from airport"
    sql += " WHERE ident = '" + idd + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

koodit = input('Anna kahden lentokentän ICAO koodi ')
a = icaokoodi(koodit)
koodit2 = input('Anna toinen ')
b = icaokoodi(koodit2)

print(distance.distance(a, b).km)

polttoaine = distance.distance(a, b).km * 0.15
print(polttoaine)