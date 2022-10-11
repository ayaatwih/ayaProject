from auth_contoller.App_Auth import App_Auth
from auth_contoller.Search_Controller import Search_controller
from model.users.Client import Client
from model.orders.Borrowing_Order import Borrowing_Order
from utils.Utils import Methods_Utils
from utils.Utils import Constants
import datetime

auth = App_Auth()
search_cont = Search_controller()

def get_user_info():
    name = input("Enter Client full name: ")
    age = input("Enter Client age: ")
    phone = input("Enter Client phone number: ")
    id_no = input("Enter Client ID number: ")
    email = input("Enter Client email: ")
    address = input("Enter Client address: ")
    password = input("Enter Client password: ")

    if Methods_Utils.check_value_is_empty(name, age, phone, email, address, password):
        print("Invaild inputs")
        return None

    clientNew = Client(id=auth.get_last_id() + 1, full_name=name, age=age, id_no=id_no, phone_number=phone,
                       email=email, address=address, password=password, )
    auth.register_new_Client(clientNew)
    print("Client added successfully")

get_user_info()

print("Welcome,please add your crediual: ")
user_name = input("Enter user name: ")
password = input("Enter password: ")


if Methods_Utils.check_value_is_empty(user_name, password):
    print("Empty fields")
    exit()

if auth.login(user_name, password):
    print("What do you want to do?")
    print("1- Search for a book")
    print("2- retrun book")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Enter the name of the book that you want: \n")
        # print book list
        book_list = auth.get_book_list()
        print("Book list: \n")
        for book in book_list:
            print(book.get_name())

        book_name = input("\nEnter book name: ")
        if Methods_Utils.check_value_is_empty(book_name):
            print("Empty field")
            exit()
        book = search_cont.search_book_by_name(book_name, auth.get_book_list())
        if book is not None:
            print("Book found")
            print(book.get_name())
            print(book.get_description())
            print(book.get_author())
            print(book.get_status())
        else:
            print("Book not found")
            exit()

        if book.get_status() == Constants.Available:
            print("please inter your ID number")
            id_no = input("Enter ID number: ")
            client_id = search_cont.search_client_by_id_no(
                id_no, auth.get_clients_list())
            if client_id is not None:
                print("Client found")
                print("welcome" + str(client_id.get_name()))
                newOrder = Borrowing_Order(order_id=1, book_id=book.get_id(
                ), clinet_id=client_id.get_id(), date=datetime.datetime.now(), status=Constants.Active)
                auth.add_new_order(newOrder)
                print("Order added")
                print("Order ID: " + str(newOrder.get_order_id()))
            else:
                print("Client not found!")
                print("Do you want to register new client? Y/N")
                answer = input("Enter answer: ")
                if answer == "Y":
                    get_user_info(auth)
                else:
                    exit()
        else:
            print("Book is not available")
            exit()

    elif choice == "2":
        print("retrun book \n")
        print("Book list: \n")
        book_list = auth.get_book_list()
        for book in book_list:
            print(book.get_name())
        book_name = input(
            "Enter the name of the book that you want to return: \n")
        if Methods_Utils.check_value_is_empty(book_name):
            print("Empty field")
            exit()
        book = search_cont.search_book_by_name(book_name, auth.get_book_list())
        if book is not None:
            print("Book found")
            print(book.get_name())
            print(book.get_description())
            print(book.get_author())
            print(book.get_status())

            print("please inter your ID number")
            id_no = input("Enter ID number: ")
            #########################################
            client_id = search_cont.search_client_by_id_no(
                id_no, auth.get_clients_list())
            if client_id is not None:
                comingOrder = search_cont.search_order_by_client_id_and_book_id(
                    id_no, book.get_id(), auth.get_orders_list())
                print("Order found")
                print(comingOrder)
                if comingOrder is not None:
                    comingOrder.set_status(Constants.Canceled)
                    print("book returned")
            else:
                print("Order not found")
                exit()
else:
    print("Wrong user name or password")
    exit()


