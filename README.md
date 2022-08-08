# skyballengine

/arjan_course_api


FUNCTIONALITY ADDED:

/hotel/db

edit_db.py 

    - Created some functions to make the changes to hotel.db file that were laid out in the challenges portion fo the course, tried a few other edits as well just out of curiousity.


/hotel/db/operations

bookings.py 

    - worked on the create_booking function as per the challenge to validate booking dates and create a booking with an available room if no vacancy for desired room.
            
    - made changes to update_booking function to account for price changes if booking's room changed.

    - created read_availability_by_date_range function to get the room numbers and ids of available rooms and get a list of rooms that are unavailable


rooms.py -


helpful_scripts.py

    - created single_date_chop function to chop parts of a single date, figured that was a repetitive task, curious if whether that merited it's own helper function.

    - created a date_range_chop function to chop up date_ranges, added functionality to treat input differently if the input is a dictionary or a string.

    - made a create_booking_dates_dict function that creates a month to days dict for each month of the year. It also strips out the leading 0's to keep it in line with integer format. It then creates a dict whose keys are the months of the booking dates and the values are the days of those months that the bookings spans.

    - made a search_years_and_months_ranges function that returns a list of unavailable rooms based on the current bookings in the system.



./

test_interface.py
    - added RoomInterface, BookingInterface, and CustomerInterface to be used during testing as subclasses of the DataInterfaceStub abstract base class, at least that's what it seemed to be but it doesn't itself inherit from the ABC class. Added mock data to the read_all methods and used that for the testing of each class.


test_bookings.py
    - added several tests 


test_customers.py -
    - added several tests


test_rooms -
    - added several tests


test_helpful_scripts -
    - added several tests
