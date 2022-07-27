from dataclasses import field
from typing import Optional
from hotel.db.engine import DBSession
from hotel.db.models import DBCustomer
from pydantic import BaseModel
from hotel.db.models import to_dict
from hotel.operations.interface import DataInterface, DataObject

class UpdateCustomerData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: Optional[str]
    address_info: Optional[str]
    market_to: Optional[bool]

class CreateCustomerData(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    address_info: str
    market_to: bool


def read_all_customers(customer_interface: DataInterface):
    return customer_interface.read_all()

def read_customer(customer_id: int, customer_interface: DataInterface):
    return customer_interface.read_by_id(customer_id)

def create_customer(data: CreateCustomerData, customer_interface: DataInterface):
    customer_dict = data.dict()
    return customer_interface.create(customer_dict)

def delete_all_customers(customer_interface: DataInterface):
    return customer_interface.delete_all()

def delete_customer(customer_id: int, customer_interface: DataInterface):
    return customer_interface.delete(customer_id)

def update_customer(customer_id: int, data: UpdateCustomerData, customer_interface: DataInterface):
    customer_data = data.dict()
    return customer_interface.update(customer_id, customer_data)
    

