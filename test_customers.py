import unittest
from test_interface import BookingInterface, RoomInterface, CustomerInterface
from hotel.operations.customers import CreateCustomerData, UpdateCustomerData, create_customer, delete_customer, update_customer

class TestCustomers(unittest.TestCase):

    def test_customers_create_if_email_exists(self) -> None:
        print()
        print("Testing test_customers_create_if_email_exists........")
        customer_data = CreateCustomerData(first_name="Billy", last_name="The Kid", email_address="btk@hotmail.com", address_info="123 Wild West Blvd.", market_to=False)
        new_customer = create_customer(customer_data, CustomerInterface())

        self.assertEqual(new_customer["id"], 4)
        

    def test_customers_update(self) -> None:
        print()
        print("Testing test_customers_update........")
        
        id = 1
        customer_data = UpdateCustomerData(
            first_name="bobby",
            last_name="sinclair",
            email_address="freebobbysin@hotmail.com",
            address_info="1234 Struggle St.",
            market_to=True,)

        updated_customer = update_customer(id, customer_data, CustomerInterface())
        self.assertEqual(customer_data.first_name, updated_customer["first_name"])

    def test_customers_delete(self) -> None:
        print()
        print("Testing test_customers_delete.........")
        id = 1
        updated_customer_list = delete_customer(id, CustomerInterface())
        self.assertEqual(len(updated_customer_list), len(CustomerInterface().read_all()) - 1)



if __name__ == "__main__":
    unittest.main()
