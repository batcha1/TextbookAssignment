from Textbook import Book
title = input("Please enter the title for book 1")
firstname = input("Please enter the author's firstname")
lastname = input("Please enter the author's lastname")
age = input("Please enter the author's age")
edition = input("Please enter the edition number")
ISBN = input("Please enter the ISBN number")
publisher = ("Please enter the publisher")
yearpublished = ("Please enter the year the book was published")
quanity = ("please enter the quanity in inventory")
price = ("Please enter the price of the book")

book1 = Book(title, firstname, lastname, age, edition,ISBN,publisher,yearpublished,quanity,price)

print("********************")
title = input("Please enter the title for book 2")
firstname = input("Please enter the author's firstname")
lastname = input("Please enter the author's lastname")
age = input("Please enter the author's age")
edition = input("Please enter the edition number")
ISBN = input("Please enter the ISBN number")
publisher = ("Please enter the publisher")
yearpublished = ("Please enter the year the book was published")
quanity = ("please enter the quanity in inventory")
price = ("Please enter the price of the book")

book2 = Book(title, firstname,lastname, age, edition,ISBN,publisher,yearpublished, quanity, price)

# Menu
menu_choice = 0

while menu_choice !=3:
        print (""""What would you like to do?"
        1. Checkin a Textbook
        2. Checkout a Textbook
        3. Modify a Textbook
        4. Quit the Program
        """)
        menu_choice = int(input())

        if menu_choice == 1:
            print("Which book 1 or 2?")
            choice = int(input())
            if choice == 1:
                quanity = int(input("How many would you like to add to inventory?"))
                book1.checkin()
                print("The quanity is now 1") +str(book1.quanity)

        elif menu_choice == 2:
            quanity = int(input("How many would you like to remove from inventory?"))
            result = book1.checkout()
            if result == 0:
                print("The quanity in inventory is now 1") + str(book1.quanity)
            else:
                print("You do not have enoughin inventory to remove that quanity")
                print("Current inventory is") + str(book1.quanity)
        elif menu_choice == 3:
            price ==float(input("What will the new price of the book be?"))
            book1.price =price
            print("The price of" + book1.title + "has been changed to" + str(book1.price))



