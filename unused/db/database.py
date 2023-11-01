import sqlite3
import datetime
from database.order_model import Order
from database.order_service import *

# conn = sqlite3.connect('order.db')
conn = sqlite3.connect('order.db')

c = conn.cursor()

# c.execute("""CREATE TABLE orders (
#             id INTEGER PRIMARY KEY,
#             order_date text,
#             customer_name text,
#             order_items text
#         )""")

current_time = datetime.datetime.now()
ord_1 = Order(current_time.strftime("%Y-%m-%d"), "華達士", "牛肉")
ord_2 = Order(current_time.strftime("%Y-%m-%d"), "弘揚", "苔")


insert_order(ord_1)
# insert_order(ord_2)
# remove_order("華達士")

order1 = get_orders("華達士")
order2 = get_orders("弘揚")

show_all()

conn.close()
close_db()
