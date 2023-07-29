from app import db

class Table(db.Model):
    __tablename__= "tables"

    id = db.Column(db.Integer, primary_key=True)
    seats = db.Column(db.String(64))

    def __repr__(self):
        return f'<Table {self.id}: {self.name}>'