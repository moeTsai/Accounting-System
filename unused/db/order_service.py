import sqlite3
import uuid

conn = sqlite3.connect('order.db')
c = conn.cursor()

def show_all():
    orders = get_orders()
    for order in orders:
        print(order)

def show_all(company_name):
    orders = get_orders(company_name)
    for order in orders:
        print(order)

def get_orders():
    return c.execute("SELECT * FROM orders").fetchall()

def get_orders(order_company):
    return c.execute("SELECT * FROM orders WHERE customer_name = :customer_name",
                     {'customer_name': order_company}).fetchall()

def insert_order(order):
    unique_id = str(uuid.uuid4())
    # print(type(unique_id))
    # print('\n\n\n\n')
    with conn:
        c.execute("INSERT INTO orders VALUES (:id, :order_date, :customer_name, :order_items)"
              , {'id': unique_id, 'order_date': order._order_date, 'customer_name': order._customer_name, 'order_items': order._order_items})
        



def update_order(order_company, order):
    with conn:
        c.execute("""UPDATE orders SET order_date = :order_date,
                customer_name = :customer_name,
                order_items = :order_items
                WHERE customer_name = :customer_name""",
                {'order_date': order._order_date, 'customer_name': order._customer_name, 'order_items': order._order_items})
              

def remove_order(id):
    with conn:
        c.execute("DELETE from orders WHERE customer_name = :customer_name",{'customer_name': order_company})


def close_db():
    conn.close()