from typing import Optional
from pydantic import BaseModel
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

def read_availability_by_room_and_date(room_id: int, res_date: str, booking_interface: DataInterface):
    
    # get parts list [year, month, day] of date to search for it's availability
    print(res_date)
    search_date = res_date.split()[0]
    print(res_date)
    pre_res_parts = search_date.split("-")
    res_parts = [i.lstrip("0") for i in pre_res_parts]
    print(res_parts)

    # get list of booking dicts
    bookings_data = booking_interface.read_all()
    print(bookings_data)

    # need a month to number of days dictionary
    days_by_month = {"1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31, "8": 21, "9": 30, "10": 31, "11": 30, "12": 31}

    # search through list of booking dicts to see if there is a booking who's from_date and to_date matchup with the date we are searching for
    for booking in bookings_data:
        if booking["room_id"] == room_id:
            pre_from_date_parts = str(booking["from_date"]).split("-")
            from_date_parts = [i.lstrip("0") for i in pre_from_date_parts]
            print(from_date_parts)

            pre_to_date_parts = str(booking["to_date"]).split("-")
            to_date_parts = [i.lstrip("0") for i in pre_to_date_parts]
            print(to_date_parts)
            year_list = [str(i) for i in range(int(from_date_parts[0]), int(to_date_parts[0]) + 1)]
            print(year_list)
            if res_parts[0] in year_list:
                print("Passed")
                month_list = [str(i) for i in range(int(from_date_parts[1]), int(to_date_parts[1]) + 1)]
                print(month_list)
                if res_parts[1] in month_list:      
                    print("Passed")
                    # create a dict whose keys are months of booking dates and whose values are the days of those months that the booking spans
                    booking_months_to_days_dict = {}
                    for i in range(len(month_list)):
                        if month_list[i] == month_list[0]: 
                            booking_months_to_days_dict.update({month_list[i]: [i for i in range(int(from_date_parts[2]), days_by_month.get(from_date_parts[1]) + 1)]})
                        elif month_list[i] == month_list[-1]:
                            booking_months_to_days_dict.update({month_list[i]: [i for i in range(1, int(to_date_parts[2]) + 1)]})
                        else:
                            booking_months_to_days_dict.update({month_list[i]: [i for i in range(1, days_by_month.get(month_list[i]) + 1)]})

                    # booking_months_to_days_dict = {month: [i for i in range(int(from_date_parts[2]), days_by_month.get(from_date_parts[1]))] if month[0] for month in month_list}
                    print(booking_months_to_days_dict)

                    # day_list = [str(i) for i in range(days_by_month[i]))) for i in month_list]
                    if res_parts[1] in booking_months_to_days_dict.keys() and int(res_parts[2]) in [i for i in booking_months_to_days_dict[res_parts[1]]]: 

                    # if (int(res_parts[2])) in [i for i in (range(int(from_date_parts[2]), int(to_date_parts[2])))]:
                        print("Passed")
                        return print("Room Unavailable")
                    continue    
                    
                continue    
                
            continue
        continue
    return print("Room Available")


            




     



