from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Image(db.Model):
  id = db.Column(db.Integer, primary_key= True)
  date = db.Column(db.Date, unique=True, nullable=False)
  image_path = db.Column(db.String(255), nullable=False)
  description = db.Column(db.Text, nullable=False)
  shown = db.Column(db.Boolean, default=False)
  
  def __repr__(self):
    return f"<Image {self.id} - {self.date}]>"