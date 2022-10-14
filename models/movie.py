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
    duration = database.Column(database.Integer)
    age_group = database.Column(database.Integer)
    launch = database.Column(database.Integer)
    trailer_video = database.Column(database.String(300))
    original_title = database.Column(database.String(100))
    synopsis = database.Column(database.String(500))
    image_url = database.Column(database.String(200))


    def __init__(self, id, name, rating, duration, age_group, launch, trailer_video, original_title, synopsis, image_url):
        self.id = id
        self.name = name
        self.rating = rating
        self.duration = duration
        self.age_group = age_group
        self.launch = launch
        self.trailer_video = trailer_video
        self.original_title = original_title
        self.synopsis = synopsis
        self.image_url = image_url

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'rating': self.rating,
            'duration': self.duration,
            'age_group': self.age_group,
            'launch': self.launch,
            'trailer_video': self.trailer_video, 
            'original_title': self.original_title,
            'synopsis': self.synopsis,
            'image_url': self.image_url
        }

    @classmethod
    def find_movie_by_id(cls, id):
        movie = cls.query.filter_by(id=id).first()
        if movie:
            return movie
        return None
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_movie(self):
        database.session.add(self)
        database.session.commit()
    
    def update_movie(self):
        database.session.merge(self)
        database.session.commit()