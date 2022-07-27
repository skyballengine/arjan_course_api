import unittest
from urllib.parse import _DefragResultBase
from hotel.operations.bookings import CreateBookingData, InvalidDateError, create_booking
from hotel.operations.interface import DataObject

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

class RoomInterface(DataInterfaceStub):
    def read_by_id(self, id: int) -> DataObject:
        return {"id": id, "number": "101", "size": 20, "price": 150}

class BookingInterface(DataInterfaceStub):
    def create(self, data: DataObject):
        booking_data = dict(data)
        booking_data["id"] = 1
        return booking_data


class TestBooking(unittest.TestCase):

    def test_price_one_day(self):
        booking_data = CreateBookingData(
            room_id=1,
            customer_id=1,
            from_date="2023-12-21",
            to_date="2023-12-29"

        )

        booking = create_booking(booking_data=booking_data, booking_interface=BookingInterface(), room_interface=RoomInterface())
        self.assertEqual(booking["price"], 1200)
        self.assertEqual(booking["id"], 1)

    def test_date_error(self):
        booking_data = CreateBookingData(
            room_id=1,
            customer_id=1,
            from_date="2023-12-29",
            to_date="2023-12-29"
        )
        self.assertRaises(InvalidDateError, create_booking, booking_data, BookingInterface(), RoomInterface())
        

if __name__ == "__main__":
    unittest.main()