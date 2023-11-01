from datetime import datetime
from order import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(200), nullable=True)
    order_items = db.Column(db.String(200), nullable=True)
    order_date = db.Column(db.String(200), nullable=False, default=datetime.utcnow().strftime('%Y-%m-%d'))
    # order_date = db.Column(db.DateTime, default=datetime.utcnow)
    
