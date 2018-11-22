from companyblog import db,loinManager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


@loinManager.user_loader    
def loadUser(user_id):
    return User.query.get(user_id)

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    profileImage = db.Column(db.Sring(20), nullable=False, default='default_profile.png')
    email = db.Column(db.Sring(64),unique=True,index = True)
    username = db.Column(db.Sring(64),unique=True,index = True)
    passwordHash = db.Column(db.Sring(128))

    posts = db.relationship('BlogPost',backref='author',lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.passwordHash = generate_password_hash(password)
    
    def checkPassword(self,password):
        return check_password_hash(self.passwordHash,password)

    def __repr__(self):
        f"Username { self.username }" 


class BlogPost():
    users = db.relationship(User)
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(160),nullable=False)
    text = db.Column(db.Text,nullable=False)

    def __init__(self,title,text,userId):
         self.title = title
         self.text = text
         self.userId = userId
    
    def __repr__(self):
        f"Post Id { self.id } -- Date: { self.date } -----{ self.title }"
     