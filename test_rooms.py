import unittest
from test_interface import BookingInterface, RoomInterface, CustomerInterface
from hotel.operations.rooms_copy import CreateRoomData

class TestRooms(unittest.TestCase):
    
    def test_read_rooms(self):
        print()
        print("Testing test_create_rooms...........")
        room_interface = RoomInterface()
        rooms = room_interface.read_all()
        assert len(rooms) == 3

    def test_check_room_availability(self):
        pass

    def test_room_properties(self):
        pass

    def test_create_room(self):
        pass




    
if __name__ == "__main__":
    unittest.main()
