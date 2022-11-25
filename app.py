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
    map_graph = text.get_map_graph()
    if (not starting_point in map_graph or not arrival_point in map_graph):
        return render_template("error.html") 
    route = text.map_text(starting_point,arrival_point)
    return render_template("service.html", route=route, route_length=len(route))

if __name__ == '__main__':
    app.run(debug=True)