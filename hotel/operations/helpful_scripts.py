
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
        
        pre_to_date = str(booking["to_date"].split()[0].split("-"))
        post_to_date = [i.lstrip("0") for i in pre_to_date]

        return post_from_date, post_to_date
    
    if isinstance(date_string, str):
        pre_from_date = date_string.split()[0].split("-")
        post_from_date = [i.lstrip("0") for i in pre_from_date]
        
        pre_to_date = date_string.split()[0].split("-")
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