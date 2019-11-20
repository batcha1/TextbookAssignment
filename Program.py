#  Aly Batch
# 11/20/19
# Textbook Programming Assignment

class Person:
    def __init__(self, firstname, lastname, age):
        self.fn = firstname
        self.ln = lastname
        self.age = age

    def description(self):
        return "The name is " + self.fn + " " + self.ln + ", and their age is " + str(self.age)

