"""
import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(200), nullable=True)
    order_items = db.Column(db.String(200), nullable=True)
    order_date = db.Column(db.String(200), nullable=False, default=datetime.utcnow)
    # order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    

    def __repr__(self):
        return '<Order %r>' % self.id
"""

class Order:
    def __init__(self, order_date, customer_name, order_items):
        print( 'initializing' )
        self._order_date = order_date
        self._customer_name = customer_name
        self._order_items = order_items

    @property
    def order_date(self):
        return self._order_date

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def order_items(self):
        return self._order_items