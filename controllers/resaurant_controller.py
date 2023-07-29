from flask import Flask, redirect, render_template, Blueprint, request
from app import db
from models import Booking, Table, Slot

restaurant_blueprint = Blueprint("restaurant", __name__)

@restaurant_blueprint.route('/the_good_restaurant/home')
def index():
    return render_template('index.jinja')


@restaurant_blueprint.route('/the_good_restaurant/book')
def show_book():
    return render_template('/customer_view/book.jinja')