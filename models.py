"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

#MODELS GO BELOW!
class User(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"


    id = db.Column(db.Integer,
                   primary_key =True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(20),
                    nullable=False,
                    unique=True)
    
    last_name = db.Column(db.String(30), nullable=False, unique=True)
    
    image_url = db.Column(db.String, nullable=False, unique=True)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")




class Post(db.Model):
    __tablename__ = 'posts'

    def __repr__(self):
        p = self
        # return f"<post_id={p.id}, title={p.title}, content={p.content}, created_at={p.created_at}>"
        return f"<post_id={p.id}, title={p.title}, content={p.content}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(20), nullable=False, unique=True)

    content =  db.Column(db.String(100), nullable=False, unique=True)

    # created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    


# strangely whenever I make a new post users_id is set to null and foreign key constriant is ignored
#and I get an annoying integrity error. 


# db.DateTime
# datetime.datetime.now