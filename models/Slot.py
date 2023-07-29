from app import db

class Slot(db.Model):

    __tablename__ = 'slots'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.String(7))
    end_time = db.Column(db.String(7))
