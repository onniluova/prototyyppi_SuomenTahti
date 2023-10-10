import mysql.connector

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