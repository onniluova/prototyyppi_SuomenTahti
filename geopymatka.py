import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'Nasslingmaga98',
    autocommit = True
)
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