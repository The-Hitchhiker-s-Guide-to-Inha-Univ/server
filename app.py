#import pyrebase
from flask import Flask, render_template
import text

config = {
    "apiKey": "AIzaSyCuaRMqPneqW0kva9WgFTDt-ubiny0n0Wc",
    "authDomain": "inhamap-69bfc.firebaseapp.com",
    "projectId": "inhamap-69bfc",
    "storageBucket": "inhamap-69bfc.appspot.com",
    "messagingSenderId": "743798326311",
    "appId": "1:743798326311:web:13b11e3e9c878cc9a87a02",
    "measurementId": "G-VTMEXV5QR6"
}

#firebase = pyrebase.initialize_app(config)

#db = firebase.daStabase()

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/map/<start>/<finish>')
def map(start = None, finish = None):
    route = text.map_text()
    return render_template("map.html", route=route, route_length=len(route))

if __name__ == '__main__':
    app.run(debug=True)