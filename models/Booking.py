from app import db

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    booking_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    number_of_guests = db.Column(db.Integer)
    date = db.Column = (db.String(64))
    tables = db.relationship('Table', backref='booking')

    def __repr__(self):
        return f'<Booking {self.id}: {self.booking_name}>'
