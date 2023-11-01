class Order:
    def __init__(self, order_date, customer_name, order_items):
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