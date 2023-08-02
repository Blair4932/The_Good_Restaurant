from app import db

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    booking_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))
    number_of_guests = db.Column(db.Integer)
    booking_date = db.Column(db.DateTime)
    accepted = db.Column(db.Boolean)
    tableid = db.Column(db.Integer, db.ForeignKey('tables.id'))
    slotid = db.Column(db.Integer, db.ForeignKey('slots.id'))

class Slot(db.Model):

    __tablename__ = 'slots'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.String(7))
    end_time = db.Column(db.String(7))
    bookings = db.relationship('Booking', backref="slot")

class Table(db.Model):
    __tablename__= "tables"

    id = db.Column(db.Integer, primary_key=True)
    seats = db.Column(db.String(64))