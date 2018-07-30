from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  first_name = db.Column(db.String(100))
  last_name = db.Column(db.String(100))
  password = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)

  def __init__(self, firstname, lastname, email, password):
    self.first_name = firstname.title()
    self.last_name = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  def set_password(self, password):
    self.password = generate_password_hash(password)


  def check_password(self, password):
    return check_password_hash(self.password, password)