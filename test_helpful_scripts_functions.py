
from datetime import date
import unittest
from hotel.operations.bookings import create_booking
from hotel.operations.helpful_scripts import create_booking_dates_dict, date_range_chop, single_date_chop
import os
import sys
from pathlib import Path

from test_interface import BookingInterface, RoomInterface

class TestHelpfulScriptsFunctions(unittest.TestCase):
    
    def test_single_date_chop(self):
        post_date = single_date_chop("2023-04-07")
        assert post_date[0] == "2023"
        assert post_date[1] == "4"
        assert post_date[2] == "7"

    def test_date_range_chop_with_string(self):
        from_dates, to_dates = date_range_chop("2024-05-06 - 2024-07-01")
        assert from_dates == ["2024", "5", "6"]
        assert to_dates == ["2024", "7", "1"]
    

    def test_date_range_chop_with_booking(self):
        booking_interface = BookingInterface()
        bookings_data = booking_interface.read_all()
        booking = bookings_data[0]
        post_dates = date_range_chop(booking)
        assert post_dates[0] == ["2023", "12", "24"]
        assert post_dates[1] == ["2023", "12", "25"]

    def test_create_booking_dates_dict(self):
        booking_interface = BookingInterface()
        bookings_data = booking_interface.read_all()
        print(bookings_data)
        
        
        assert bookings_data[0]["room_id"] == 1
        assert bookings_data[1]["customer_id"] == 2
        assert type(bookings_data[2]["from_date"]) == date
        assert type(bookings_data[0]["to_date"]) == date
        assert bookings_data[1]["cancel_able"] == True


if __name__ == "__main__":
    unittest.main()



