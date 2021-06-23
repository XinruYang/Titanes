import json
from flask import Flask
import os, sys

ruta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ruta)

from streamlit import config
from utils_.flask_functions import funcion_flask_1

def mi_funcion():
    print(funcion_flask_1())


if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def home():
        with open(os.path.dirname(ruta) + '/data/googleplaystore.json', 'r+') as json_file:
            google_play_store = json.load(json_file)
        return google_play_store

    with open(os.path.dirname(ruta) + '/config/flask_settings.json', 'r+') as json_file:
        config = json.load(json_file)
    
    app.run(
        host = config['host'],
        port = config['port'],
        debug =config['debug']
    )