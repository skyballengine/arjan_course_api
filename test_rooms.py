import unittest
from hotel.operations.rooms import UpdateRoomData, create_room, read_room, update_room
from test_interface import BookingInterface, RoomInterface, CustomerInterface
from hotel.operations.rooms import CreateRoomData, read_availability_by_room_and_date

class TestRooms(unittest.TestCase):
    
    def test_read_rooms(self):
        print()
        print("Testing test_read_rooms...........")
        room_interface = RoomInterface()
        rooms = room_interface.read_all()
        self.assertEqual(len(rooms), 3)
        self.assertEqual(int(rooms[0]["number"]), 10)

    def test_read_availability_by_room_and_date(self):
        print()
        print("Testing test_read_availability_by_room_and_date.........")
        room_id = 3
        res_date = "2023-11-25"
        booking_interface = BookingInterface()
        is_available = read_availability_by_room_and_date(room_id, res_date, booking_interface)
        self.assertEqual(is_available, False)

    def test_update_room(self):
        print()
        print("Testing test_update_room............")
        room_id = 1
        new_room_data = UpdateRoomData(
            number="15",
            size=350,
            price=750,
            amenities="Cleaning Supplies, XL Mini Fridge, New Stuff"
        )
        not_updated_room = read_room(room_id, RoomInterface())
        updated_room = update_room(room_id, new_room_data, RoomInterface())
        self.assertNotEqual(not_updated_room, updated_room)

    def test_create_room(self):
        print()
        print("Testing test_create_room........")
        new_room = CreateRoomData(
            number="1000",
            size=1500,
            price=10000,
            amenities="Everything"
        )
        new_all_rooms = create_room(new_room, RoomInterface())
        self.assertEqual(new_all_rooms[-1], dict(new_room))


    
if __name__ == "__main__":
    unittest.main()
