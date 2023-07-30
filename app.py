from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://blairscott@localhost:5432/good_restaurant2"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Slot, Table, Booking
from controllers.resaurant_controller import restaurant_blueprint

app.register_blueprint(restaurant_blueprint)

@app.route('/')
def home():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)