"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

#MODELS GO BELOW!
class User(db.Model):
    __tablename__ = 'users'

    # @classmethod
    # def get_by_species(cls, species):
    #     return cls.query.filter_by(species=species).all()
    #     # call -----> Pet.get_by_species('lizard')

    # @classmethod
    # def get_all_hungry(cls):
    #     return cls.query.filter(Pet.hunger > 20).all()


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

    # def greet(self):
    #     return f"Hola, I am {self.name} the {self.species}"

    # def feed(self, amt=20):
    #     """Update hunger based off of amount"""
    #     self.hunger -= amt
    #     self.hunger = max(self.hunger, 0)
