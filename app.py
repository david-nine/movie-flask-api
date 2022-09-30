from flask import Flask
from flask_restful import Resource, Api
from resources.movies import Movies, Movie

app = Flask(__name__)
api = Api(app)
    
api.add_resource(Movies, '/movies')
api.add_resource(Movie, '/movies/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)