import random
class Noppa:

    def nopanHeitto(self, rahat, ilmastopisteet, polttoaine, message):
        noppa = random.randint(1, 12)

        if noppa == 1:
            print("Lentokoneessa on vikaa. Korjaus maksaa 100€")
            rahat -= 100

        elif noppa ==2:
            raha_lista=[100,200,300]
            raha_maara = random.randint(0,2)
            rahat += raha_lista[raha_maara]
            message = "Löysit rahaa. Sait " + str(raha_lista[raha_maara]) + "€"

        elif noppa ==3:
            message = "Lensit ekologisesti. Sait 10 ilmastopistettä."
            ilmastopisteet += 10

        elif noppa == 4:
            message = ("Sinut ryöstettiin. Menetit 100€")
            rahat -= 100

        elif noppa == 5:
            message = "Lentokoneessa on vikaa. Korjaus maksaa 100€"
            rahat -= 100

        elif noppa in range(6,11):
            polttoaine -= 0
            message = "Ei tapahdu mitään"

        elif noppa == 12:
            message = "Löysit aarteen! Sait 150€ ja 10 ilmastopistettä"
            ilmastopisteet += 10
            rahat += 100
        #Nopan heitto ja tapahtuma
        return rahat, ilmastopisteet, polttoaine, message
