import unittest
from urllib.parse import _DefragResultBase

from h11 import Data
from hotel.operations.bookings import CreateBookingData, InvalidDateError, create_booking
from hotel.operations.interface import DataObject
from test_bookings import BookingInterface, RoomInterface

class DataInterfaceStub:
    def read_by_id(self, id: int) -> DataObject:
        raise NotImplementedError()

    def read_all(self) -> DataObject:
        raise NotImplementedError()

    def create(self, data: DataObject) -> DataObject:
        raise NotImplementedError()
    
    def update(self, id: int, data: DataObject):
        raise NotImplementedError()

    def delete(self, id: int) -> DataObject:
        raise NotImplementedError()

class BookingInterface(DataInterfaceStub):
    def create_mock_booking(self):
        booking_data = CreateBookingData(room_id=1, customer_id=2, from_date="2022-11-01", to_date="2022-11-10", cancel_able=True)
        booking_data = booking_data.dict()
        return booking_data



class TestHelperFunctions(unittest.TestCase):

    def test_single_date_chop(self):
        booking_data = CreateBookingData(room_id=1, customer_id=2, from_date="2022-11-01", to_date="2022-11-10", cancel_able=True)
        booking = create_booking(booking_data, booking_interface=BookingInterface(), room_interface=RoomInterface())

mock_booking = BookingInterface()
mock_booking.create_mock_booking()