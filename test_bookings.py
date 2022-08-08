import unittest
from hotel.operations.bookings import CreateBookingData, InvalidDateError, create_booking
from hotel.operations.interface import DataObject
from test_interface import BookingInterface, RoomInterface



class TestBooking(unittest.TestCase):

    def test_price_one_day(self) -> None:
        print()
        print(f"Testing test_price_one_day .........")

        booking_data = CreateBookingData(
            room_id=1,
            customer_id=1,
            from_date="2023-12-24",
            to_date="2023-12-25",
            cancel_able=True

        )

        
        booking = create_booking(booking_data, BookingInterface(), RoomInterface())
    
        
        self.assertEqual(booking["price"], 75)
        self.assertEqual(booking["id"], 4)

    def test_date_error(self) -> None:
        print()
        print("Testing test_date_error .........")
        booking_data = CreateBookingData(
            room_id=1,
            customer_id=1,
            from_date="2023-12-29",
            to_date="2023-12-29",
            cancel_able=True
        )
        self.assertRaises(InvalidDateError, create_booking, booking_data, BookingInterface(), RoomInterface())

    def test_create_booking_with_no_vacancy(self) -> None:
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
        # program should automatically assign the first vacant room it finds because room with room_id from the booking data is already occupied
        self.assertNotEqual(booking["room_id"], 2)

        
    def test_create_booking(self) -> None:
        print()
        print(f"Testing test_create_booking .........")
        
        booking_data = CreateBookingData(
            room_id=1,
            customer_id=1,
            from_date="2022-09-23",
            to_date="2022-10-02",
            cancel_able=True
        )
        
        booking = create_booking(booking_data, BookingInterface(), RoomInterface())
        self.assertEqual(booking["room_id"], 1)
    

if __name__ == "__main__":
    unittest.main()