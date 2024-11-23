from database import db
from datetime import datetime

class Meals(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.now())
    isOnDiet = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "datetime": self.datetime,
            "isOnDiet": self.isOnDiet,
        }