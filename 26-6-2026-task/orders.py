from dbconnection import get_connection
import json

def place_order(customer, product, amount, metadata):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO orders(customer_name, product_name, amount, metadata) VALUES (%s,%s,%s,%s) RETURNING order_id;"
        cursor.execute(query,(customer,product,amount,json.dumps(metadata)))
        order_id = cursor.fetchone()[0]
        conn.commit()
        print(f"Order created with ID {order_id}")
    except Exception as e:
        conn.rollback()
        print("Order failed. Rolled back.")
        print(e)
    finally:
        cursor.close()
        conn.close()

def get_by_customer(customer):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM orders WHERE customer_name=%s;"
        cursor.execute(query,(customer,))
        orders = cursor.fetchall()
        print(f"{"ID":<2} {"Name":<12} {"Product":<10} {"Quantity":<12} {"Status":<15} {"Metadata":<50} {"TimeStamp":<30}")
        for order in orders:
            print(f"{order[0]:<2} {order[1]:<12} {order[2]:<10} {order[3]:<12} {order[4]:<15} {str(order[5]):<50} {str(order[6]):<30}")
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        cursor.close()
        conn.close()

def update_status(order_id, new_status):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "UPDATE orders SET status=%s WHERE order_id=%s;"
        cursor.execute(query,(new_status,order_id))
        conn.commit()
        print("Status updated")
    except Exception as e:
        conn.rollback()
        print("Update failed")
        print(e)
    finally:
        cursor.close()
        conn.close()

def delete_order(order_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "DELETE FROM orders WHERE order_id=%s;"
        cursor.execute(query,(order_id,))
        conn.commit()
        print("Order deleted")
    except Exception as e:
        conn.rollback()
        print("Delete failed")
        print(e)
    finally:
        cursor.close()
        conn.close()

def view_orders():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM orders;"
        cursor.execute(query)
        orders = cursor.fetchall()
        print(f"{"ID":<2} {"Name":<12} {"Product":<10} {"Quantity":<12} {"Status":<15} {"Metadata":<50} {"TimeStamp":<30}")
        for order in orders:
            print(f"{order[0]:<2} {order[1]:<12} {order[2]:<10} {order[3]:<12} {order[4]:<15} {str(order[5]):<50} {str(order[6]):<30}")
    except Exception as e:
        conn.rollback()
        print("Error:",e)
    finally:
        cursor.close()
        conn.close()