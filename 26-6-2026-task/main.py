# DAILY TASK- WEEK 4- DAY 2
'''
✓ Connect to PostgreSQL — create orders table (SERIAL, TIMESTAMP)
✓ Write: place order, get by customer, update status, delete
✓ Use transactions — rollback on any failure
✓ Store JSONB metadata field per order
✓ Push to GitHub — compare MySQL vs PostgreSQL code in README'''

from orders import *
import json

print("\nORDER MANAGEMENT SYSTEM")
print("""
1. Place Order
2. Get Orders By Customer
3. Update Order Status
4. Delete Order
5. View all orders
6. Exit
""")

while True:
    choice = int(input("\nEnter your choice: "))
    match choice:
        case 1:
            print("\nPlace New Order")
            customer = input("Customer Name: ")
            product = input("Product Name: ")
            amount = float(input("Amount: "))
            payment = input("Payment Method: ")
            coupon = input("Coupon Code (Enter None if no coupon): ")
            gift = input("Gift Wrap (yes/no): ").lower() == "yes"
            metadata = {
                "payment": payment,
                "coupon": coupon,
                "gift": gift
            }
            place_order(customer,product,amount,metadata)

        case 2:
            customer = input("Enter Customer Name: ")
            print("\nCustomer Orders\n")
            get_by_customer(customer)

        case 3:
            order_id = int(input("Order ID: "))
            status = input("New Status: ")
            update_status(order_id,status)

        case 4:
            order_id = int(input("Order ID to delete: "))
            delete_order(order_id)

        case 5:
            print("Viewing all orders..")
            view_orders()

        case 6:
            print("Exiting...")
            break

        case _:
            print("Invalid Choice")