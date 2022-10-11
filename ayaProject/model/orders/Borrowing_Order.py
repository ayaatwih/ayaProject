class Borrowing_Order:
    def __init__(self, order_id, book_id, clinet_id, date, status):
        self.order_id = order_id
        self.book_id = book_id
        self.clinet_id = clinet_id
        self.date = date
        self.status = status

    def get_order_id(self):
        return self.order_id

    def get_book_id(self):
        return self.book_id

    def get_client_id(self):
        return self.clinet_id

    def get_date(self):
        return self.date

    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status