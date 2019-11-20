from Program import Person
class Textbook:
    def __init__(self, title, firstname, lastname, age, edition, ISBN, publisher, yearpublished, quanity, price):
        self.author = Person(firstname,lastname,age)
        self.title = title
        self.edition = edition
        self.ISBN = ISBN
        self.publisher = publisher
        self.yearpublished = yearpublished
        self.quanity = quanity
        self.price = price

