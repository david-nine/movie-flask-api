from random import choices
from time import time
from flask_restful import Resource, reqparse
import datetime
from models.movie import GenderType
from models.user import UserModel

default_users = [
    {
        'id': 1,
        'name': 'David Hildebrandt',
        'born_date': datetime.date(1998, 10, 5).strftime('%Y-%m-%d'),
        'gender': 'male',
        'email': 'david@gmail.com',
        'profile_photo_url': 'https://avatars.githubusercontent.com/u/54282964?v=4'
    }
]

class Users(Resource):
    
    def get(self):
        return UserModel.find_all(), 200

class User(Resource):

    request = reqparse.RequestParser()
    request.add_argument('name', type=str)
    request.add_argument('born_date', type=datetime.date, required=True)
    request.add_argument('gender', type=str, choices=[i.name.lower() for i in GenderType])
    request.add_argument('email', type=int)
    request.add_argument('profile_photo_url', type=int)

    def find_user_by_id(id):
        return UserModel.find_user_by_id(id)

    def find_last_user_id():
        user_id = 0
        for user in default_users:
            if user['id'] >= user_id:
                user_id = user['id']
        return user_id

    def get(self, id: int):
        user = User.find_user_by_id(id)
        if user:
            return user.json()
        return {'message': 'user not found'}, 200

    def post(self, id):
        data = self.request.parse_args()
        user_id = User.find_last_movie_id() + 1
        new_user = UserModel(user_id, **data)
        
        new_user.save_user()

        return new_user.json(), 201

    def put(self, id):
        user = User.find_user_by_id(id)
        data = self.request.parse_args()
        if user:
            new_user = UserModel(id, **data)
            new_user.save_user()
        else:
            new_user = self.post(id)[0]
        return new_user.json(), 201


    def delete(self, id):
        movie = User.find_user(id)
        if movie:
            default_users.remove()
            return {}, 200
        else:
            return 'User not found', 404