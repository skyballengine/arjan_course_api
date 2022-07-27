
from ..operations.helpful_scripts import create_booking_dates_dict, dates_chop
from ..operations.interface import DataInterface
from ..db.db_interface import DBInterface
from ..db.models import DBBooking
import os
import sys
from pathlib import Path



print(os.getcwd())
HERE = Path(__file__).parent
print(HERE)
booking_interface = DBInterface(DBBooking)
date_parts = dates_chop(booking_interface)
print(date_parts)