from flask_restful import Resource, reqparse
from models.movie import MovieModel

movies = [
    {
        'id': 1,
        'name': 'Home Aranha 3',
        'rating': 3.5,
        'duration': 120,
        'launch': 2015,
        'age_group': 14,
        'trailer_video': 'https://www.youtube.com/watch?v=3OmZujBbMOg',
        'original_title': 'Spider Man 3',
        'synopsis': 'O relacionamento entre Peter Parker e Mary Jane parece estar dando certo, mas outros problemas começam a surgir. A roupa de Homem-Aranha torna-se preta e acaba controlando Peter - apesar de aumentar seus poderes, ela revela e amplia o lado obscuro de sua personalidade. Com isso, os vilões Venom e Homem-Areia tentam destruir o herói.',
        'image_url': 'https://www.sonypictures.com.br/sites/brazil/files/2022-03/KEY%20ART_HOMEM%20ARANHA%203.JPG'
    },   
    {
        'id': 2,
        'name': 'Dois filhos de francisco',
        'rating': 5.0,
        'duration': 140,
        'launch': 2016,
        'age_group': 16,
        'trailer_video': 'https://www.youtube.com/watch?v=M1vzU3kCcaU',
        'original_title': 'Dois filhos de francisco',
        'synopsis': 'Depois de superar a perda do irmão, Mirosmar tenta seguir carreira solo em São Paulo, mas sem sucesso. Quando Francisco vê o interesse de Welson pela música, ele volta a acreditar em seu sonho. A recém-formada dupla adota o nome artístico de Zezé Di Camargo e Luciano.',
        'image_url': 'https://br.web.img3.acsta.net/medias/nmedia/18/91/61/69/20155011.jpg'
    },   
    {
        'id': 3,
        'name': 'Top Gun : Ases Indomáveis',
        'rating': 4.5,
        'duration': 150,
        'launch': 2022,
        'age_group': 16,
        'trailer_video': 'https://www.youtube.com/watch?v=9Jgua93Xhcw',
        'original_title': 'Top Gun: Maverick',
        'synopsis': 'Depois de mais de 30 anos de serviço como um dos principais aviadores da Marinha, Pete "Maverick" Mitchell está de volta, rompendo os limites como um piloto de testes corajoso. No mundo contemporâneo das guerras tecnológicas, Maverick enfrenta drones e prova que o fator humano ainda é essencial.',
        'image_url': 'https://s2.glbimg.com/Uocz4wbYTe75W0oI1puLqCu8-l0=/362x536/https://s2.glbimg.com/WxMMnW_-6pGqMdoD3DWXGtcr0ww=/i.s3.glbimg.com/v1/AUTH_c3c606ff68e7478091d1ca496f9c5625/internal_photos/bs/2021/R/f/YAMCmvSnyYIt4zP4v2Zg/1534951-poster.jpg'
    }
]

class Movies(Resource):
    
    def get(self):
        return MovieModel.find_all(), 200

class Movie(Resource):

    request = reqparse.RequestParser()
    request.add_argument('name', type=str, required=True)
    request.add_argument('rating', type=float)
    request.add_argument('duration', type=int, required=True)
    request.add_argument('launch', type=int)
    request.add_argument('age_group', type=int)
    request.add_argument('trailer_video', type=str)
    request.add_argument('original_title', type=str)
    request.add_argument('synopsis', type=str)
    request.add_argument('image_url', type=str)


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
        new_movie.save_movie()

        return new_movie.json(), 201

    def put(self, id):
        movie = Movie.find_movie(id)
        data = self.request.parse_args()
        if movie:
            new_movie = MovieModel(id, **data)
            new_movie.update_movie()
        else:
            new_movie = {
                'id': Movie.find_last_movie_id() + 1,
                'name': data['name'],
                'rating': data['rating'],
                'duration': data['duration'],
                'launch': data['launch'],
                'age_group': data['name'],
                'trailer_video': data['rating'],
                'original_title': data['duration'],
                'synopsis': data['launch'],
                'image_url': data['launch']
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