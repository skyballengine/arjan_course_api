from typing import Optional
from pydantic import BaseModel
from datetime import date
from hotel.operations.helpful_scripts import date_range_chop, search_years_and_months_ranges, single_date_chop
from hotel.operations.interface import DataInterface, DataObject

class InvalidDateError(Exception):
    pass

class DatesUnavailable(Exception):
    pass

class UpdateBookingData(BaseModel):
    room_id: Optional[int]
    customer_id: Optional[int]
    from_date: Optional[date]
    to_date: Optional[date]
    cancel_able: Optional[bool]

class CreateBookingData(BaseModel):
    room_id: int
    customer_id: int
    from_date: date
    to_date: date
    cancel_able: bool

# The two classes below are unused
class ReadRoomAvailabilityByRoomAndDate(BaseModel):
    room_id: int
    from_date: date
    to_date: date

class ReadRoomAvailabilityByDateRange(BaseModel):
    from_date: date
    to_date: date


def read_all_bookings(booking_interface: DataInterface) -> list[DataObject]:
    return booking_interface.read_all()
    

def read_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.read_by_id(booking_id)


def create_booking(booking_data: CreateBookingData, booking_interface: DataInterface, room_interface: DataInterface) -> DataObject:
    
    room = room_interface.read_by_id(booking_data.room_id)

    days = (booking_data.to_date - booking_data.from_date).days
    if days <= 0:
        raise InvalidDateError("Invalid number of days.")

    booking_dict = booking_data.dict()
    booking_dict["price"] = room["price"] * days


    # validate dates of booking
    date_string = f"{str(booking_dict['from_date'])} - {str(booking_dict['to_date'])}" 
    print(date_string)
    room_ids, room_numbers, unavailable_rooms = read_availability_by_date_range(date_string, booking_interface, room_interface)
    print(f"A list of room id's: {room_ids}, Room numbers: {room_numbers}, and Unavailable Rooms: {unavailable_rooms}")
    room = room_interface.read_by_id(booking_dict["room_id"])
    print(f"Desired room info is: {room}")
    room_num = room["number"]
    print(f"Room number is: {room_num}")

    try:
        if room["id"] in unavailable_rooms:
            raise DatesUnavailable
        print("Desired room available, booking being created.....")
        return booking_interface.create(booking_dict)

    except DatesUnavailable:
        print(f"Dates not available for Room {room_num}")
        new_room_id = room_ids[0]
        booking_dict.update({"room_id": new_room_id})
        room_number = room_interface.read_by_id(new_room_id)["number"]
        print(f"New room found: Room Number {room_number}, we know you'll love it! ;)")
        return booking_interface.create(booking_dict)
        


def update_booking(booking_id: int, booking_data: UpdateBookingData, booking_interface: DataInterface) -> DataObject:
    booking_dict = booking_data.dict()
    return booking_interface.update(booking_id, booking_dict)

def delete_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.delete(booking_id)

def delete_all_bookings(booking_interface: DataInterface) -> DataObject:
    return booking_interface.delete_all()

def read_availability_by_date_range(date_range: str, booking_interface: DataInterface, room_interface: DataInterface) -> DataObject:
    bookings_data = booking_interface.read_all()
    rooms_data = room_interface.read_all()
    all_rooms = [i["id"] for i in rooms_data]
    print(f"All room id's: {all_rooms}")

    unavailable_rooms = search_years_and_months_ranges(bookings_data, date_range)
    print(unavailable_rooms)

    # find the difference between all rooms in bookings and unavailable rooms 
    available_rooms = set(all_rooms).difference(set(unavailable_rooms))
    room_ids = [room_interface.read_by_id(room_id)["id"] for room_id in available_rooms]

    # now we get room numbers once we have the list of room_id's
    room_numbers = [room_interface.read_by_id(room_id)["number"] for room_id in room_ids]

    print(f"The following rooms are available: {room_numbers}")
    return room_ids, room_numbers, unavailable_rooms
