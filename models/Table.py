from app import db

class Table(db.Model):
    __tablename__= "tables"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'))

    def __repr__(self):
        return f'<Table {self.id}: {self.name}>'