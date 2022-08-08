from typing import Optional
from pydantic import BaseModel
from hotel.operations.helpful_scripts import create_booking_dates_dict, single_date_chop
from hotel.operations.interface import DataInterface


class CreateRoomData(BaseModel):
    number: str
    size: int
    price: int
    amenities: str

class UpdateRoomData(BaseModel):
    number: Optional[str]
    size: Optional[int]
    price: Optional[int]
    amenities: Optional[str]



def read_all_rooms(room_interface: DataInterface):
    return room_interface.read_all()

def read_room(room_id: int, room_interface: DataInterface):
    return room_interface.read_by_id(room_id)

def update_room(room_id: int, data: UpdateRoomData, room_interface: DataInterface):
    room_data = data.dict()
    return room_interface.update(room_id, room_data)

def create_room(room_data: CreateRoomData, room_interface: DataInterface):
    room_data_dict = room_data.dict()
    return room_interface.create(room_data_dict)

def read_availability_by_room_and_date(room_id: int, res_date: str, booking_interface: DataInterface):
    
    # get parts list [year, month, day] of date to search for it's availability
    res_parts = single_date_chop(res_date)

    # get list of booking dicts
    bookings_data = booking_interface.read_all()

    # search through list of booking dicts to see if there is a booking who's from_date and to_date matchup with the date we are searching for
    for booking in bookings_data:
        if booking["room_id"] == room_id:
            booking_months_to_days_dict = create_booking_dates_dict(booking)
            if res_parts[1] in booking_months_to_days_dict.keys() and int(res_parts[2]) in [i for i in booking_months_to_days_dict[res_parts[1]]]:
                print("Room Unavailable")
                return False
            continue        
        continue
    print("Room Available")
    return True

