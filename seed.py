# from app import db
# from models import Table, Slot
# import click

# from flask.cli import with_appcontext

# @click.command(name='seed')
# @with_appcontext
# def seed():
#     Table.query.delete()
#     Slot.query.delete()
#     slot1 = Slot(start_time='5pm', end_time='5:30pm')
#     slot2 = Slot(start_time='5:30pm', end_time='6pm')
#     slot3 = Slot(start_time='6pm', end_time='6:30pm')
#     slot4 = Slot(start_time='6:30pm', end_time='7pm')
#     slot5 = Slot(start_time='7pm', end_time='7:30pm')
#     slot6 = Slot(start_time='7:30pm', end_time='8pm')
#     slot7 = Slot(start_time='8pm', end_time='8:30pm')
#     slot8 = Slot(start_time='8:30pm', end_time='9pm')

#     table1 = Table(seats=4)
#     table2 = Table(seats=2)
#     table3 = Table(seats=6)
#     table4 = Table(seats=2)
#     table5 = Table(seats=4)
#     table6 = Table(seats=4)
#     table7 = Table(seats=10)
#     table8 = Table(seats=8)
#     table9 = Table(seats=4)
#     table10 = Table(seats=4)

#     db.session.add(slot1)
#     db.session.add(slot2)
#     db.session.add(slot3)
#     db.session.add(slot4)
#     db.session.add(slot5)
#     db.session.add(slot6)
#     db.session.add(slot7)
#     db.session.add(slot8)

#     db.session.add(table1)
#     db.session.add(table2)
#     db.session.add(table3)
#     db.session.add(table4)
#     db.session.add(table5)
#     db.session.add(table6)
#     db.session.add(table7)
#     db.session.add(table8)
#     db.session.add(table9)
#     db.session.add(table10)
#     db.session.commit()