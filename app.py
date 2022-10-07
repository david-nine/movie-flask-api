from flask import Flask
from flask_restful import Api
from resources.movies import Movies, Movie
from sql_alchemy import database

app = Flask(__name__)
api = Api(app)

DATABASE_URI = 'mysql+pymysql://root@localhost/movie?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_database():
    database.create_all()

api.add_resource(Movies, '/movies')
api.add_resource(Movie, '/movies/<int:id>')

if __name__ == '__main__':
    database.init_app(app)
    app.run(debug=True)