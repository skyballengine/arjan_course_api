from datetime import datetime
from fastapi import APIRouter
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBBooking, DBRoom
from hotel.operations.rooms_copy import CreateRoomData, UpdateRoomData, read_all_rooms, read_availability_by_room_and_date, read_room, update_room, create_room
router = APIRouter()

@router.get("/rooms")
def api_read_all_rooms():
    room_interface = DBInterface(DBRoom)
    return read_all_rooms(room_interface)

@router.get("/room/{room_id}")
def api_read_room(room_id: int):
    room_interface = DBInterface(DBRoom)
    return read_room(room_id, room_interface)

@router.post("/room/{room_id}")
def api_update_room(room_id: int, data: UpdateRoomData):
    room_interface = DBInterface(DBRoom)
    return update_room(room_id, data, room_interface)

@router.get("/room/availability/{room_id}/{res_date}")
def api_check_room_availability_by_room_and_date(room_id: int, res_date: str):
    booking_interface = DBInterface(DBBooking)
    return read_availability_by_room_and_date(room_id, res_date, booking_interface)

@router.post("/createroom")
def api_create_room(data: CreateRoomData):
    room_interface = DBInterface(DBRoom)
    return create_room(data, room_interface)