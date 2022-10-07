from flask_restful import Resource, reqparse
from models.movie import MovieModel

movies = [
    {
        'id': 1,
        'name': 'Home Aranha 3',
        'rating': 3.5,
        'duration': 120,
        'created_at': 2015
    },   
    {
        'id': 2,
        'name': 'Dois filhos de francisco',
        'rating': 5.0,
        'duration': 140,
        'created_at': 2016
    },   
    {
        'id': 3,
        'name': 'Top Gun : Ases Indomáveis',
        'rating': 4.5,
        'duration': 150,
        'created_at': 2022
    }   
]

class Movies(Resource):
    
    def get(self):
        return movies

class Movie(Resource):

    request = reqparse.RequestParser()
    request.add_argument('name', type=str, required=True)
    request.add_argument('rating', type=float)
    request.add_argument('duration', type=int, required=True)
    request.add_argument('created_at', type=int)

    def find_movie(id):
        return MovieModel.find_movie_by_id(id)

    def find_last_movie_id():
        movie_id = 0
        for movie in movies:
            if movie['id'] >= movie_id:
                movie_id = movie['id']
        return movie_id

    def get(self, id: int):
        movie = Movie.find_movie(id)
        if movie:
            return movie.json()
        return {'message': 'movie not found'}, 200

    def post(self, id):
        data = self.request.parse_args()
        movie_id = Movie.find_last_movie_id() + 1
        new_movie = MovieModel(movie_id, **data)
        
        movies.append(new_movie.json())

        return new_movie.json(), 201

    def put(self, id):
        movie = Movie.find_movie(id)
        data = self.request.parse_args()
        if movie:
            new_movie = MovieModel(id, **data)
            movies.append(new_movie.json())
            movies.remove(movie)
        else:
            new_movie = {
                'id': Movie.find_last_movie_id() + 1,
                'name': data['name'],
                'rating': data['rating'],
                'duration': data['duration'],
                'created_at': data['created_at']
            }
            movies.append(new_movie.json())
        return new_movie.json(), 201


    def delete(self, id):
        movie = Movie.find_movie(id)
        if movie:
            movies.remove()
            return {}, 200
        else:
            return 'Movie not found', 404