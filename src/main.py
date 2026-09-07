from customers.customer_manager import CustomerManager

# Initial dictionary of customers (students will enhance this later)
customers = {
    "cust_101": {"name": "Alice", "location": "New York", "purchases": ["Laptop", "Mouse"]},
    "cust_102": {"name": "Bob", "location": "Los Angeles", "purchases": ["Phone", "Charger"]},
    "cust_103": {"name": "Charlie", "location": "New York", "purchases": ["Tablet", "Headphones"]}
}

customer_manager = CustomerManager(customers)

print("\nAll Customers:")
customer_manager.display_customers()

# Filtering is not yet implemented (students will add it)
print("\nFiltered Customers:")
customer_manager.filter_customers_by_city("New York")

# Unique locations are not yet implemented (students will add them)
print("\nUnique Locations:")
customer_manager.get_unique_locations()

print("\nUpdate Customer Location:")
customer_manager.update_customer_location("cust_102", "San Francisco")

customer_manager.get_unique_locations()