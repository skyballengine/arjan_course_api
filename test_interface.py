import unittest
from hotel.operations.bookings import CreateBookingData, InvalidDateError, create_booking
from hotel.operations.customers import CreateCustomerData
from hotel.operations.interface import DataObject
from hotel.operations.rooms import CreateRoomData
from datetime import datetime, date

class DataInterfaceStub:
    def read_by_id(self, id: int) -> DataObject:
        raise NotImplementedError()

    def read_all(self) -> DataObject:
        raise NotImplementedError()

    def create(self, data: DataObject) -> DataObject:
        raise NotImplementedError()
    
    def update(self, id: int, data: DataObject):
        raise NotImplementedError()

    def delete(self, id: int) -> DataObject:
        raise NotImplementedError()

class RoomInterface(DataInterfaceStub):
    def read_by_id(self, id: int) -> DataObject:
        room_data = self.read_all()
        for room in room_data:
            if room["id"] == id:
                return room

    def create(self, data: DataObject) -> list[dict]:
        all_rooms = self.read_all()
        all_rooms.append(data)
        return all_rooms

    def update(self, id: int, data: DataObject) -> list[dict]:
        result = [customer for customer in self.read_all() if customer["id"] == id][0]
        print(f"Before update: {result}")
        for key, value in data.items():
            if key in result.keys():
                result.update({key: value})
        
        print(f"After update: {result}")
        return result
    
    # create mock rooms
    def read_all(self) -> list[dict]:
        
        room_1 = CreateRoomData(
            number="10",
            size=300,
            price=75,
            amenities="Cleaning Supplies, XL Mini Fridge"
        )

        room_2 = CreateRoomData(
            number="15",
            size=400,
            price=275,
            amenities="Four Seasons Decor"
        )

        room_3 = CreateRoomData(
            number="20",
            size=500,
            price=750,
            amenities="Gold Plated Everything"
        )

        rooms_list = []
        rooms_list.append(dict(room_1))
        rooms_list.append(dict(room_2))
        rooms_list.append(dict(room_3))

        new_id = 1
        for room in rooms_list:
            room.update(id=new_id)
            new_id += 1
        
        return rooms_list
        

class BookingInterface(DataInterfaceStub):
    def create(self, data: DataObject):
        booking_data = dict(data)
        booking_data["id"] = len(self.read_all()) + 1
        print(booking_data)
        return booking_data

    # create mock bookings
    def read_all(self) -> list[dict]:
        bookings_list = []
        booking_1 = CreateBookingData(
            room_id=1,
            customer_id=1,
            from_date="2023-12-24",
            to_date="2023-12-25",
            cancel_able=True

        )
        booking_2 = CreateBookingData(
            room_id=2,
            customer_id=2,
            from_date="2023-10-24",
            to_date="2023-10-25",
            cancel_able=True

        )

        booking_3 = CreateBookingData(
            room_id=3,
            customer_id=3,
            from_date="2023-11-24",
            to_date="2023-12-01",
            cancel_able=True

        )

        bookings_list.append(dict(booking_1))
        bookings_list.append(dict(booking_2))
        bookings_list.append(dict(booking_3))

        new_id = 1
        for booking in bookings_list:
            booking.update(id=new_id)
            new_id += 1


        return bookings_list

class CustomerInterface(DataInterfaceStub):
    def create(self, customer_data: DataObject) -> DataObject:
        customer_data["id"] = len(self.read_all()) + 1
        print(customer_data)
        return customer_data

    def update(self, id: int, data: DataObject) -> list[dict]:
        result = [customer for customer in self.read_all() if customer["id"] == id][0]
        print(f"Before update: {result}")
        for key, value in data.items():
            if key in result.keys():
                result.update({key: value})
        
        print(f"After update: {result}")
        return result

    def delete(self, id: int) -> list[dict]:
        results = self.read_all()
        print(f"Before deletion of customer {id}: {results}")
        for customer in results:
            if customer["id"] == id:
                deleted_customer = customer
                results.remove(customer)
        print(f"The customer: {deleted_customer} was deleted from the list.") 
        return results
        



    # create mock customers
    def read_all(self) -> list[dict]:
        customer_1 = CreateCustomerData(
            first_name="Bobby",
            last_name="Sinclair",
            email_address="freebobbysin@hotmail.com",
            address_info="123 Struggle St.",
            market_to=True,
        )
        customer_2 = CreateCustomerData(
            first_name="Wilma",
            last_name="Sinclair",
            email_address="wilmasin@hotmail.com",
            address_info="456 Struggle St.",
            market_to=True,
        )
        customer_3 = CreateCustomerData(
            first_name="Frannie Sue",
            last_name="Sinclair",
            email_address="frannysin@hotmail.com",
            address_info="789 The Ave.",
            market_to=True,
        )
        customer_list = []
        customer_list.append(dict(customer_1))
        customer_list.append(dict(customer_2))
        customer_list.append(dict(customer_3))

        new_id = 1 
        for customer in customer_list:
            customer.update(id=new_id)
            new_id += 1


        return customer_list