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
    game_instance.haeKentät()
    status = {
        'rahat': game_instance.rahat,
        'polttoaine': game_instance.polttoaine,
        'ilmastopisteet': game_instance.ilmastopisteet,
        'kilometrit': game_instance.kilometrit,
        'nykyinenSijainti': game_instance.nykyinenSijainti.nimi,
    }
    return jsonify(status), 200

# Tarvittaessa lisätään muita reittejä

if __name__ == '__main__':
    app.run(debug=True)