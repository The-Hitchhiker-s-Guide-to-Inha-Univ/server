from flask import Flask, render_template
import text

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