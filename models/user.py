from sql_alchemy import database

class UserModel (database.Model):

    __tablename__ = 'user'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255))
    born_date = database.Column(database.Date)
    gender = database.Column(database.String(6))
    email = database.Column(database.String(255))
    profile_photo_url = database.Column(database.String(255))


    def __init__(self, id, name, born_date, gender, email, profile_photo_url):
        self.id = id
        self.name = name
        self.born_date = born_date
        self.gender = gender
        self.email = email
        self.profile_photo_url = profile_photo_url

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'born_date': self.born_date.striptime(),
            'gender': self.gender,
            'email': self.email,
            'profile_photo_url': self.profile_photo_url
        }

    @classmethod
    def find_user_by_id(cls, id):
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None
  
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_user(self):
        database.session.add(self)
        database.session.commit()    
    
    def delete(self):
        database.session.delete(self)
        database.session.commit()
    
    def update_user(self):
        database.session.merge(self)
        database.session.commit()