from numbers import Number
from model.users.Client import Client
from model.books.Book import Book
from model.orders.Borrowing_Order import Borrowing_Order

class Search_controller:

    def search_for_client_by_id(self, id: int, client_list: list[Client]):
        if client_list == None or len(client_list) == 0:
            return None
        else:
              for item in client_list:
                 if item.get_id() == id:
                      return item


    def search_book_by_name(self, name: str, book_list: list[Book]):
        if book_list == None or len(book_list) == 0:
            return None
        else:
            for item in book_list:
                if item.get_name() == name:
                    return item

    def search_client_by_id_no(self, id_num: int, client_list: list[Client]):
        if client_list == None or len(client_list) == 0:
            return None
        else:
            for item in client_list:
                if item.get_id_no() == id_num:
                    return item

    def search_order_by_client_id_and_book_id(self, client_id: int, book_id: int, order_list: list[Borrowing_Order]):
        if order_list == None or len(order_list) == 0:
            return None
        else:
            for item in order_list:
                if item.get_client_id() == client_id and item.get_book_id() == book_id:
                    return item