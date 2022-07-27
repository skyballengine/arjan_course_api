
# chop up dates and make useable
from datetime import date
from hotel.operations.interface import DataObject


def single_date_chop(res_date: str) -> list[str]:
    search_date = res_date.split()[0]
    pre_res_parts = search_date.split("-")
    return [i.lstrip("0") for i in pre_res_parts]



def date_range_chop(booking: DataObject = None, date_string: str = None) -> tuple[list]:

    if isinstance(booking, dict):
        pre_from_date = str(booking["from_date"]).split("-")
        post_from_date = [i.lstrip("0") for i in pre_from_date]
        
        pre_to_date = str(booking["to_date"]).split("-")
        post_to_date = [i.lstrip("0") for i in pre_to_date]

        return post_from_date, post_to_date
    
    if isinstance(date_string, str):
        pre_from_date = date_string.split("-")
        post_from_date = [i.lstrip("0") for i in pre_from_date]
        
        pre_to_date = date_string.split("-")
        post_to_date = [i.lstrip("0") for i in pre_to_date]

        return post_from_date, post_to_date



# pass in a single booking
def create_booking_dates_dict(booking: DataObject):

    # need a month to number of days dictionary
    DAYS_BY_MONTH = {"1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31, "8": 21, "9": 30, "10": 31, "11": 30, "12": 31}

    # create a dictionary of months (keys) and days as lists of integers (values)
    pre_from_date_parts = str(booking["from_date"]).split("-")
    from_date_parts = [i.lstrip("0") for i in pre_from_date_parts]

    pre_to_date_parts = str(booking["to_date"]).split("-")
    to_date_parts = [i.lstrip("0") for i in pre_to_date_parts]
    
    year_list = [str(i) for i in range(int(from_date_parts[0]), int(to_date_parts[0]) + 1)]
    
    month_list = [str(i) for i in range(int(from_date_parts[1]), int(to_date_parts[1]) + 1)]
   
    
    # create a dict whose keys are months of booking dates and whose values are the days of those months that the booking spans
    booking_months_to_days_dict = {}
    for i in range(len(month_list)):
        if month_list[i] == month_list[0]: 
            booking_months_to_days_dict.update({month_list[i]: [i for i in range(int(from_date_parts[2]), DAYS_BY_MONTH.get(from_date_parts[1]) + 1)]})
        elif month_list[i] == month_list[-1]:
            booking_months_to_days_dict.update({month_list[i]: [i for i in range(1, int(to_date_parts[2]) + 1)]})
        else:
            booking_months_to_days_dict.update({month_list[i]: [i for i in range(1, DAYS_BY_MONTH.get(month_list[i]) + 1)]})


    return booking_months_to_days_dict

def search_years_and_months_ranges(bookings_data, date_range):
    # create a dict with from_date and to_date to use later
    date_range_parts = date_range.split(" - ")
    date_range_dict = {"from_date": date_range_parts[0], "to_date": date_range_parts[1]}

    # create unavailable and total rooms lists, BUT still need the room numbers which we can get at the end of the function
    unavailable_rooms = []

    # create from_date parts from date_range
    from_date_range = date_range_dict["from_date"]
    from_date_range_parts_int = [int(x) for x in single_date_chop(from_date_range)]

    # create to_date parts from date_range
    to_date_range = date_range_dict["to_date"]
    to_date_range_parts_int = [int(y) for y in single_date_chop(to_date_range)]

    #TODO create a helper function to perform this action, good challenge and it's too messy as is - check __contains__ built in method for range to see if it can vbe sused for our purposes
    for booking in bookings_data:
        from_date_parts, to_date_parts = date_range_chop(booking)
        booking_from_date_parts_int = [int(i) for i in from_date_parts]
        booking_to_date_parts_int = [int(i) for i in to_date_parts]
        # using range we can see if the SEARCH year, month, and day range are within the BOOKING year, month, and day ranges

        search_year_range = [i for i in range(from_date_range_parts_int[0], to_date_range_parts_int[0])]
        booking_year_range = [j for j in range(booking_from_date_parts_int[0], booking_to_date_parts_int[0])]
        
        search_month_range = [i for i in range(from_date_range_parts_int[1], to_date_range_parts_int[1])]
        booking_month_range = [i for i in range(booking_from_date_parts_int[1], booking_to_date_parts_int[1])]

        day_range = set(range(booking_from_date_parts_int[2], booking_to_date_parts_int[2])).intersection(set(range(from_date_range_parts_int[2], to_date_range_parts_int[2])))

        if len(set(search_year_range).intersection(set(booking_year_range))) >= 1:
            if len(set(search_month_range).intersection(set(booking_month_range))) >= 1:
                if len(day_range) >= 1:
                    unavailable_rooms.append(booking["room_id"])
                continue
            continue
        continue
    return unavailable_rooms







        # if range(from_date_range_parts_int[0], to_date_range_parts_int[0]) == range(booking_from_date_parts_int[0], booking_to_date_parts_int[0]) or range(from_date_range_parts_int[0], to_date_range_parts_int[0]) in range(booking_from_date_parts_int[0], booking_to_date_parts_int[0]):
        #     if range(from_date_range_parts_int[1], to_date_range_parts_int[1]) == range(booking_from_date_parts_int[1], booking_to_date_parts_int[1]) or range(from_date_range_parts_int[1], to_date_range_parts_int[1]) in range(booking_from_date_parts_int[1], booking_to_date_parts_int[1]):             
        #         day_range = set(range(booking_from_date_parts_int[2], booking_to_date_parts_int[2])).intersection(set(range(from_date_range_parts_int[2], to_date_range_parts_int[2])))
        #         if len(day_range) >= 1:
        #             unavailable_rooms.append(booking["room_id"])
        #         continue
                
        #     continue
        # continue
