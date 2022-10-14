from sql_alchemy import database
from enum import Enum

class GenderType(Enum):
    male = 1
    female = 2

class MovieModel (database.Model):

    __tablename__ = 'movies'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50))
    rating = database.Column(database.String(5))
    durarion = database.Column(database.Integer)


    def __init__(self, id, name, rating, durarion):
        self.id = id
        self.name = name
        self.rating = rating
        self.durarion = durarion

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'rating': self.rating,
            'duration': self.duration
        }

    @classmethod
    def find_movie_by_id(cls, id):
        movie = cls.query.filter_by(id=id).first()
        if movie:
            return movie
        return None
    
    def save_movie(self):
        database.session.add(self)
        database.session.commit()