class Client:

    def __init__(self, id, full_name, age, id_no, phone_number, email, address, password):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

    def get_id(self):
        return self.id

    def get_name(self):
        return self.full_name

    def get_password(self):
        return self.password

    def get_age(self):
        return self.age

    def get_id_no(self):
        return self.id_no

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address