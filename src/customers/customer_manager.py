class CustomerManager:
    def __init__(self, customers):
        self.customers = customers

    def display_customers(self, customers=None):
        """Displays all customer records, or a given subset if provided."""
        customers = customers if customers is not None else self.customers
        for cust_id, details in customers.items():
            print(f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}")

    def filter_customers_by_city(self, city):
        filtered_customers = {cust_id: details for cust_id, details in self.customers.items() if details["location"].lower() == city.lower()}

        if filtered_customers:
            print(f"\nCustomers in {city}:")
            self.display_customers(filtered_customers)
        else:
            print(f"\nNo customers found in {city}.")

    def get_unique_locations(self):
        custom_locations = {customer["location"] for customer in self.customers.values()}
        print("\nUnique Customer Locations:", custom_locations)

    def update_customer_location(self, customer_id, new_location):
        if customer_id in self.customers:
            old_location = self.customers[customer_id]["location"]
            self.customers[customer_id]["location"] = new_location
            print(f"\nUpdated {self.customers[customer_id]["name"]}'s location from {old_location} to {new_location}.")
        else: 
            print("\nCustomer not found.")