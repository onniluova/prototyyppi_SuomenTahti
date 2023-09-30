#Satunnaiset tapahtumat. Näistä tapahtuu aina yksi laskeuduttuasi uuteen kohteeseen. Määräytyy 12-sivuisen nopan heiton tuloksen mukaan.
    #• Nopan luku yksi: Koneeseesi tulee vika ja se täytyy korjata ennen seuraavaan paikkaan siirtymistä. Voit joko maksaa 100 euroa, tai heittää noppaa. Yli kolmella saa tankattua ilmaiseksi. Jos nopan luku on alle kolme, odotat vuoron.
    #• Nopan luku kaksi: Löydät rahaa. Voit löytää 100, 200 tai 300 euroa liikkumastasi paikasta. Jokaisella on sama mahdollisuus. (1/3)
    #• Nopan luku kolme: Myötätuuli. Menetit 50% vähemmän polttoainetta.
    #• Nopan luku neljä: Sinut ryöstetään. Menetät 100 euroa.
    #• Nopan luku viisi. Sää on liian huono. Et pysty lentämään ja olet hotellissa yötä. Maksat 100 euroa hotellista.
    #• Nopan luku 6-11: Ei tapahdu mitään.
    #• Nopan luku 12: Löydät paikallisen Tokmannin. Saat sieltä ämpärin. Ämpäri lisää ilmastopisteitä 100 pisteellä.




    # SQL- kyselyt:
    # Paikkakunnat : select municipality from airport, country
    # where airport.iso_country = country.iso_country and country.name = "Finland"

import random
def sattuma(noppa):

    if noppa == 1:
        print("Lentokoneessa on vikaa. Se täytyy korjata")

    elif noppa ==2:
        raha_lista=[100,200,300]
        raha_maara = random.randint(0,2)
        print(f"Löysit {raha_lista[raha_maara]}€")

    elif noppa ==3:
        print("Myötätuuli")

    elif noppa == 4:
        print("Sinut ryöstettiin. Menetit 100€")

    elif noppa == 5:
        print("Sää on liian huono lentämiseen. Joudut yöpymään hotellissa. -100€")

    elif noppa in range(6,11):
        print("Ei tapahdu mitään")

    elif noppa == 12:
        print("ÄMPÄRIARVONTA!!")





    return


noppa = random.randint(1,12)
print(noppa)

print(sattuma(noppa))