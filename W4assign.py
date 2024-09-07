#Creating a Python class named Person.
class Person:

#Creating attributes: Name, age, and gender for the class person
    def __init__(intro, name, age, gender):
        intro.name = name
        intro.age = age
        intro.gender = gender

#Implementing a method called introduce that prints a message introducing the person with their name, age, and gender.
    def introduce(intro):
        print(f"Hello, my name is {intro.name}. I am {intro.age} years old and my gender is {intro.gender}.")

# Creating an instance of the Person class
person = Person(name="Francis", age=35, gender="Male")

# Calling the introduce method to display the person's information
person.introduce()