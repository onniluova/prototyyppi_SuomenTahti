from flask import Flask, jsonify
import peli

app = Flask(__name__)

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
        'nykyinenSijainti': game_instance.nykyinenSijainti.nimi,
    }
    return jsonify(status), 200
@app.route('/haeKentat', methods=['GET'])
def haeKentat():
    game_instance.haeKentät()
    airport_details = {
        airport_id: {
            'nimi': airport.nimi,
            'longitude': airport.longitude,
            'latitude': airport.latitude
        } for airport_id, airport in game_instance.lentoasema_lista.items()
    }
    return jsonify(airport_details), 200


# Tarvittaessa lisätään muita reittejä

if __name__ == '__main__':
    app.run(debug=True)