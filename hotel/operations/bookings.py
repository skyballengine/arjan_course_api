from typing import Optional
from pydantic import BaseModel
from datetime import date
from hotel.operations.helpful_scripts import single_date_chop
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
    room_ids, room_numbers, unavailable_rooms = read_availability_by_date_range(date_string, booking_interface, room_interface)
    print(room_ids, room_numbers, unavailable_rooms)
    room = room_interface.read_by_id(booking_dict["room_id"])
    print(room)
    room_num = room["number"]
    print(room_num)

    try:
        if room["id"] not in unavailable_rooms:
            # booking creation
            return booking_interface.create(booking_dict)

    except DatesUnavailable:
        print(f"Dates not available for Room {room_num}")
        new_room_id = room_ids[0]
        booking_dict.update({"room_id": new_room_id})
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


    # create a dict with from_date and to_date to use later
    date_range_parts = date_range.split(" - ")
    date_range_dict = {"from_date": date_range_parts[0], "to_date": date_range_parts[1]}

    # create unavailable and total rooms lists, BUT still need the room numbers which we can get at the end of the function
    unavailable_rooms = []
    all_rooms = [i["id"] for i in rooms_data]

    # create from_date parts from date_range
    from_date_range = date_range_dict["from_date"]
    from_date_range_parts = from_date_range.split("-")
    from_date_range_parts_int = [int(x) for x in from_date_range_parts]
    
    # create to_date parts from date_range
    to_date_range = date_range_dict["to_date"]
    to_date_range_parts = to_date_range.split("-")
    to_date_range_parts_int = [int(y) for y in to_date_range_parts]

    for booking in bookings_data:
        from_date_parts = str(booking["from_date"]).split("-")
        from_date_parts_int = [int(i) for i in from_date_parts]
        to_date_parts = str(booking["to_date"]).split("-")
        to_date_parts_int = [int(j) for j in to_date_parts]

        if range(from_date_parts_int[0], to_date_parts_int[0]) == range(from_date_range_parts_int[0], to_date_range_parts_int[0]):
            if range(from_date_parts_int[1], to_date_parts_int[1]) == range(from_date_range_parts_int[1], to_date_range_parts_int[1]):             
                day_range = set(range(from_date_parts_int[2], to_date_parts_int[2])).intersection(set(range(from_date_range_parts_int[2], to_date_range_parts_int[2])))
                if len(day_range) >= 1:
                    unavailable_rooms.append(booking["room_id"])
                continue
                
            continue
        continue

    # find the difference between all rooms in bookings and unavailable rooms 
    # print(all_rooms, unavailable_rooms)
    available_rooms = set(all_rooms).difference(set(unavailable_rooms))
    room_ids = [room_interface.read_by_id(room_id)["id"] for room_id in available_rooms]
    print(room_ids)

    # now we get room numbers once we have the list of room_id's
    room_numbers = [room_interface.read_by_id(room_id)["number"] for room_id in room_ids]
    #print(room_numbers)

    print(f"The following rooms are available: {room_numbers}")
    return room_ids, room_numbers, unavailable_rooms


