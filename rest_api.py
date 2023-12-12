from flask import Flask, jsonify
from flask_cors import CORS  # Import the CORS library
import peli

app = Flask(__name__)
CORS(app)
# Tehdään peli instanssi
game_instance = None

@app.route('/luoPeli', methods=['GET'])
def luoPeli():
    global game_instance
    game_instance = peli.Peli()
    return jsonify(message="Uusi peli luotu"), 200

@app.route('/getStatus', methods=['GET'])
def getStatus():
    status = {
        'rahat': game_instance.rahat,
        'polttoaine': game_instance.polttoaine,
        'ilmastopisteet': game_instance.ilmastopisteet,
        'kilometrit': game_instance.kilometrit,
        'nykyinenSijainti': game_instance.nykyinenSijainti.id,
    }
    return jsonify(status), 200

@app.route('/haeSaatiedot/<airport_id>', methods=['GET'])
def haeSaatiedot(airport_id):
    sää = game_instance.palautaSäänTiedot(airport_id)
    return jsonify(sää), 200

@app.route('/haeKentat', methods=['GET'])
def haeKentat():
    game_instance.haeKentät()
    airport_details = {
        airport_id: {
            'nimi': airport.nimi,
            'longitude': airport.longitude,
            'latitude': airport.latitude,
        } for airport_id, airport in game_instance.lentoasema_lista.items()
    }
    return jsonify(airport_details), 200

@app.route('/haeMahdolliset', methods=['GET'])
def haeMahdolliset():
    mahdolliset_kohteet = game_instance.haeMahdollisetKentät()
    airport_details = {
        airport.id: {
            'nimi': airport.nimi,
            'longitude': airport.longitude,
            'latitude': airport.latitude,
        } for airport in mahdolliset_kohteet
    }
    return jsonify(airport_details), 200

@app.route('/siirry/<airport_id>', methods=['GET'])
def siirry(airport_id):
    game_instance.siirryKohteeseen(airport_id)
    status = {
        'rahat': game_instance.rahat,
        'polttoaine': game_instance.polttoaine,
        'ilmastopisteet': game_instance.ilmastopisteet,
        'kilometrit': game_instance.kilometrit,
        'nykyinenSijainti': game_instance.nykyinenSijainti.municipality,
    }
    return jsonify(status), 200

@app.route('/noppa', methods=['GET'])
def noppa():
    game_instance.heitaNoppaa()
    noppa = {
            'rahat': game_instance.rahat,
            'ilmastopisteet': game_instance.ilmastopisteet,
            'polttoaine': game_instance.polttoaine,
            'message': game_instance.message,
    }
    return jsonify(noppa), 200
@app.route('/tankkaustiedot', methods=['GET'])
def tankkaustiedot():
    game_instance.tankkaus()
    tankkaus = {
            'rahat': game_instance.rahat,
            'ilmastopisteet': game_instance.ilmastopisteet,
            'polttoaine': game_instance.polttoaine
    }
    return jsonify(tankkaus), 200
# Tarvittaessa lisätään muita reittejä

if __name__ == '__main__':
    app.run(debug=True)
