from venv import create
from fastapi import APIRouter
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBBooking, DBCustomer
from hotel.operations.customers import CreateCustomerData, UpdateCustomerData, delete_all_customers, delete_customer, read_all_customers, read_customer, create_customer, update_customer

router = APIRouter()

@router.get("/customers")
def api_read_all_customers():
    customer_interface = DBInterface(DBCustomer)
    return read_all_customers(customer_interface)

@router.get("/customer/{customer_id}")
def api_read_customer(customer_id: int):
    customer_interface = DBInterface(DBCustomer)
    return read_customer(customer_id, customer_interface)

@router.post("/customer")
def api_create_customer(data: CreateCustomerData):
    customer_interface = DBInterface(DBCustomer)
    return create_customer(data, customer_interface)

@router.delete("/customers")
def api_delete_all_customers():
    customer_interface = DBInterface(DBCustomer)
    return delete_all_customers(customer_interface)

@router.delete("/customer/{customer_id}")
def api_delete_customer(customer_id: int):
    customer_interface = DBInterface(DBCustomer)
    return delete_customer(customer_id, customer_interface)

@router.post("/customer/{customer_id}")
def api_update_customer(customer_id: int, data: UpdateCustomerData):
    customer_interface = DBInterface(DBCustomer)
    return update_customer(customer_id, data, customer_interface)
