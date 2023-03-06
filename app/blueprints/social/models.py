from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(120), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    pokemons = db.relationship('Pokemon', backref='poke', lazy='dynamic')


    def __repr__(self): #for developer
        return f'<User: {self.username}>'
    
    def __str__(self): #what the user sees
        return f'User: {self.email}|{self.username}'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def commit(self):
        db.session.add(self)
        db.session.commit()

    # def from_dict(self,a_dict):
    #     self.username=a_dict['username']
    #     self.email=a_dict['email']

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post: {self.body}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon_name = db.Column(db.String(50), nullable=False)
    pokemon_type = db.Column(db.String(50), nullable=False)
    pokemon_weight = db.Column(db.Integer, nullable=False)
    pokemon_abilities = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def commit(self):
        db.session.add(self)
        db.session.commit()


