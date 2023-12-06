import random
import mysql.connector
from geopy import distance
class lentokenttä:
    def __init__(self, nimi, longitude, latitude, municipality, id = "EFHK"):
        self.nimi = nimi
        self.id = id
        self.longitude = longitude
        self.latitude = latitude
        self.municipality = municipality

def muunnaKunta(municipality):
    # Split the string at '/' and take the first part
    primary_municipality = municipality.split('/')[0].strip()
    # Replace spaces with underscores
    return primary_municipality.replace(" ", "_")

def kohteet():
    yhteys = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='lentokonepeli',
        user='root',
        password='1234',
        autocommit=True
    )

    sql = "SELECT airport.name, longitude_deg, latitude_deg, airport.ident, municipality FROM airport"
    sql += " inner join country on country.iso_country = airport.iso_country where country.name =" + "'Finland'" + " AND type = 'medium_airport'"
    sql += " order by latitude_deg"
    sql += " LIMIT 26"
    lentokentta_lista = {}
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        muunnettu_municipality = muunnaKunta(rivi[4])
        lentoasema = lentokenttä(rivi[0], rivi[1], rivi[2], muunnettu_municipality, rivi[3])
        lentokentta_lista.update({rivi[3]: lentoasema})
    return lentokentta_lista

#lista = kohteet()
#print(lista)