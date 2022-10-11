class Book:

    def __init__(self, id, title, description, author, status):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.status = status

    def get_id(self):
        return self.id

    def get_name(self):
        return self.title

    def get_description(self):
        return self.description

    def get_author(self):
        return self.author

    def get_status(self):
        return self.status
