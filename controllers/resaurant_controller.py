from flask import Flask, redirect, render_template, Blueprint, request
from app import db
from models import Booking, Slot, Table

restaurant_blueprint = Blueprint("restaurant", __name__)

@restaurant_blueprint.route('/the_good_restaurant/home')
def index():
    return render_template('index.jinja')

@restaurant_blueprint.route('/the_good_restaurant/book')
def show_book():
    slots = Slot.query.all()
    return render_template('/customer_view/book.jinja', slots=slots)

@restaurant_blueprint.route('/the_good_restaurant/booking-confirmed')
def booking_confirmed():
    bookings = Booking.query.all()
    return render_template('/customer_view/booking_confirmed.jinja', bookings=bookings)

@restaurant_blueprint.route('/the_good_restaurant/bookings')
def show_bookings():
    slots = Slot.query.all()
    bookings = Booking.query.all()
    tables = Table.query.all()
    return render_template('/staff-view/bookings.jinja', slots=slots, bookings=bookings, tables=tables)

@restaurant_blueprint.route("/the_good_restaurant/book", methods=['POST'])
def create_booking():
    bookings = Booking.query.all()
    booking_name = request.form['booking_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    number_of_guests = request.form['number_of_guests']
    date = request.form['date']
    slot = request.form['slot']
    for booking in bookings: 
        if slot == booking.slotid and date == booking.booking_date:
            return render_template('/the_good_restaurant/home')
    else:
        booking = Booking(booking_name=booking_name, email=email, phone_number=phone_number, booking_date=date, number_of_guests=number_of_guests, slotid=slot)
    db.session.add(booking)
    db.session.commit()
    return render_template('/customer_view/booking_confirmed.jinja')

@restaurant_blueprint.route("/the_good_restaurant/show_booking/<id>") 
def show_booking(id):
    booking = Booking.query.get(id)
    return render_template('/staff-view/show_booking.jinja', booking=booking, id=id)

@restaurant_blueprint.route("/the_good_restaurant/show_booking/<id>/delete", methods=['POST']) 
def delete_booking(id):
    booking = Booking.query.get(id)
    db.session.delete(booking)
    db.session.commit()
    return redirect('/the_good_restaurant/bookings')

@restaurant_blueprint.route('/the_good_restaurant/<id>/edit')
def show_edit(id):
    booking = Booking.query.get(id)
    slots = Slot.query.all()
    return render_template('/staff-view/edit.jinja', slots=slots, booking=booking, id=id)

@restaurant_blueprint.route('/the_good_restaurant/<id>/edit', methods=['POST'])
def update_booking(id):
    booking_name = request.form['booking_name']
    email = request.form['email']
    number_of_guests = request.form['number_of_guests']
    phone_number = request.form['phone_number']
    date = request.form['date']
    
    booking = Booking.query.get(id)
    booking.booking_name = booking_name
    booking.email = email
    booking.number_of_guests = number_of_guests
    booking.phone_number = phone_number
    booking.date = date
    
    db.session.commit()
    return redirect('/the_good_restaurant/bookings')