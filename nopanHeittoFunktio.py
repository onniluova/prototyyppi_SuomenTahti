import random
class Noppa:

    def nopanHeitto(self, rahat, ilmastopisteet, polttoaine):
        noppa = random.randint(1, 12)

        if noppa == 1:
            print("Lentokoneessa on vikaa. Korjaus maksaa 100€")
            rahat -= 100

        elif noppa ==2:
            raha_lista=[100,200,300]
            raha_maara = random.randint(0,2)
            rahat += raha_lista[raha_maara]
            print(f"Löysit {raha_lista[raha_maara]}€")

        elif noppa ==3:
            print("Lensit ekologisesti. Sait 10 ilmastopistettä.")
            ilmastopisteet += 10

        elif noppa == 4:
            print("Sinut ryöstettiin. Menetit 100€")
            rahat -= 100

        elif noppa == 5:
            print("Lentokoneessa on vikaa. Korjaus maksaa 100€")
            rahat -= 100

        elif noppa in range(6,11):
            polttoaine -= 0
            print("Ei tapahdu mitään")

        elif noppa == 12:
            print("ÄMPÄRIARVONTA!!")
            ilmastopisteet += 50
            rahat += 250
        #Nopan heitto ja tapahtuma
        return rahat, ilmastopisteet, polttoaine

# Compare this snippet from siirryKohteeseen.py: