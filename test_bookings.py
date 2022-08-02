import unittest
from hotel.operations.bookings_copy import CreateBookingData, InvalidDateError, create_booking
from hotel.operations.interface import DataObject
from test_interface import BookingInterface, RoomInterface



class TestBooking(unittest.TestCase):

    def test_price_one_day(self):
        print()
        print(f"Testing test_price_one_day .........")

        booking_data = CreateBookingData(
            room_id=1,
            customer_id=1,
            from_date="2023-12-24",
            to_date="2023-12-25",
            cancel_able=True

        )

        
        booking = create_booking(booking_data=booking_data, booking_interface=BookingInterface(), room_interface=RoomInterface())
    
        
        self.assertEqual(booking["price"], 75)
        self.assertEqual(booking["id"], 1)

    def test_date_error(self):
        print()
        print(f"Testing test_date_error .........")
        booking_data = CreateBookingData(
            room_id=1,
            customer_id=1,
            from_date="2023-12-29",
            to_date="2023-12-29",
            cancel_able=True
        )
        self.assertRaises(InvalidDateError, create_booking, booking_data, BookingInterface(), RoomInterface())

    def test_create_booking_with_no_vacancy(self):
        print()
        print(f"Testing test_create_booking_with_no_vacancy .........")
    
        booking_data = CreateBookingData(
            room_id=2,
            customer_id=1,
            from_date="2023-10-24",
            to_date="2023-10-25",
            cancel_able=True
        )
        booking = create_booking(booking_data, BookingInterface(), RoomInterface())
        assert booking["room_id"] != 2

        
    def test_create_booking(self):
        print()
        print(f"Testing test_create_booking .........")
        
        booking_data = CreateBookingData(
            room_id=1,
            customer_id=1,
            from_date="2023-10-23",
            to_date="2023-10-25",
            cancel_able=True
        )
        
        booking = create_booking(booking_data, BookingInterface(), RoomInterface())
    

if __name__ == "__main__":
    unittest.main()