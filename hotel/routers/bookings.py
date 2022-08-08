from fastapi import APIRouter
from hotel.db.models import DBBooking, DBRoom
from hotel.operations.bookings import CreateBookingData, ReadRoomAvailabilityByDateRange, UpdateBookingData, read_availability_by_date_range, update_booking, create_booking, delete_booking, delete_all_bookings, read_all_bookings, read_booking, delete_booking
from hotel.db.db_interface import DataObject, DBInterface
router = APIRouter()

@router.get("/bookings")
def api_read_all_bookings():
    database_interface = DBInterface(DBBooking)
    return read_all_bookings(database_interface)

@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int):
    booking_interface = DBInterface(DBBooking)
    return read_booking(booking_id, booking_interface)

@router.post("/booking")
def api_create_booking(booking_data: CreateBookingData):
    booking_interface = DBInterface(DBBooking)
    room_interface = DBInterface(DBRoom)
    return create_booking(booking_data, booking_interface, room_interface)

@router.delete("/bookings")
def api_delete_all_bookings():
    booking_interface = DBInterface(DBBooking)
    return delete_all_bookings(booking_interface)

@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int):
    booking_interface = DBInterface(DBBooking)
    return delete_booking(booking_id, booking_interface)

@router.post("/booking/{booking_id}")
def api_update_booking(booking_id: int, booking_data: UpdateBookingData):
    booking_interface = DBInterface(DBBooking)
    return update_booking(booking_id, booking_data, booking_interface)

@router.get("/bookings/available-rooms/{date_range}")
def api_read_availability_by_date_range(date_range: str):
    booking_interface = DBInterface(DBBooking)
    room_interface = DBInterface(DBRoom)
    return read_availability_by_date_range(date_range, booking_interface, room_interface)
