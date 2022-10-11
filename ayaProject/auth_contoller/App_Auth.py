from model.users.Client import Client
from model.users.Librarian import Librarian
from model.books.Book import Book
from model.orders.Borrowing_Order import Borrowing_Order
from utils.Utils import Constants


class App_Auth:

    Clients_list: list[Client] = [
        # id, full_name, age, id_no, phone_number, email, address, password
        Client(1, "ibrahim", 21, "7878", '0592862591',
               "brhmhelou@gmail.com", "Gaza - Palestine", "ibra"),
    ]

    Librarians_list: list[Librarian] = [
        # id, full_name, age, id_no, eployment_type
        Librarian(1, "Aya", 23, "0592267756", Constants.Full_time),
    ]

    Book_List: list[Book] = [
        #id,         title,          description,      author,       status
        Book(1, "The Alchemist", "this book is good",
             "HarperCollins", Constants.Available),
        Book(2, "The Maze Runner", "this book is amzing",
             "James Dashner", Constants.Not_available),
    ]

    Borrowing_Order_List: list[Borrowing_Order] = [
        Borrowing_Order(1, 1, "7878", "2022-10-10", Constants.Active),
    ]

    def get_last_id(self) -> int:
        return self.Clients_list[len(self.Clients_list) - 1].get_id()

    def get_last_order_id(self):
        return self.Borrowing_Order_List[len(self.Borrowing_Order_List) - 1].get_id()

    def register_new_Client(self, client):
        self.Clients_list.append(client)

    def add_new_order(self, order):
        self.Borrowing_Order_List.append(order)

    def return_book(self, book_id):
        for book in self.Book_List:
            if book.get_id() == book_id:
                book.set_status(Constants.Inactive)
                return True
        return False

    def get_borrowing_order_list(self):
        return self.Borrowing_Order_List

    def login(self, user_name: str, password: str) -> bool:
        for item in self.Clients_list:
            if item.get_name() == user_name and item.get_password() == password:
                return True
        return False

    def get_book_list(self):
        return self.Book_List

    def get_clients_list(self):
        return self.Clients_list

    def get_orders_list(self):
        return self.Borrowing_Order_List
