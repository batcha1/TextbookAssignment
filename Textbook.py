from Program import Person
class Book:
    def __init__(self, title, firstname, lastname, age, edition, ISBN, publisher, yearpublished, quanity, price):
        self.author = Person(firstname,lastname,age)
        self.title = title
        self.edition = edition
        self.ISBN = ISBN
        self.publisher = publisher
        self.yearpublished = yearpublished
        self.quanity = quanity
        self.price = price

    def checkout(self):
        self.quanity - 1

        if self.quanity < 5:
            return "WARNING! Book count is low, currently have " + self.quanity

        return "0"

    def checkin(self):
        self.quanity + 1
        print("Book has been checked in!")

    def checkInventory(self):
        print(f"Current inventory is {self.quanity}!")





