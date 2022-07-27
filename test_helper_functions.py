
from hotel.operations.helpful_scripts import create_booking_dates_dict, dates_chop
from hotel.operations.interface import DataInterface
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBBooking
import os
import sys
from pathlib import Path

# TODO need a connection with the database to get bookings data
booking_interface = DBInterface(DBBooking)
date_parts = dates_chop(booking_interface)
print(date_parts)




