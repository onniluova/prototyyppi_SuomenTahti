#select airport.name,municipality, latitude_deg, longitude_deg from airport
#where airport.iso_country in(select country.iso_country from country
#where country.name = "Finland")
#