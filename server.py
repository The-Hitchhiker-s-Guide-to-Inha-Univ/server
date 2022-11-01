from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/map/<start>/<finish>')
def map(start = None, finish = None):
    return render_template("map.html", start=start, finish=finish)

if __name__ == '__main__':
    app.run(debug=True)
