from flask import Flask, render_template, request
import text

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/map',methods=['get'])
def map():
    starting_point = request.args.get('starting_point')
    arrival_point = request.args.get('arrival_point')
    print(f'starting point : {starting_point}, arrival point : {arrival_point}')
    route = text.map_text(starting_point,arrival_point)
    return render_template("map.html", route=route, route_length=len(route))

if __name__ == '__main__':
    app.run(debug=True)