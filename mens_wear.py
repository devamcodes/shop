"""
Project:
Author:Devam A

Description:By importing the three shop functions in this file and changing few lines a proper shop program is created
status:ongoing.
"""

from utils import database
from cryptography.fernet import Fernet, MultiFernet
main_menu = """
1. Purchase Apparels
2. Purchase Trousers
3. Purchase Shoes
4. View Cart
5. Exit The Program
"""


user_names = []
user_name = input("enter your name:-")
user_name_bool = bool(user_name)
if user_name_bool:
    print(f"Welcome!! To the cloths shop, {user_name.title()}")

else:
    raise ValueError("Invalid Name!! Please try again...")

user_names.append(user_name)
user_id = len(user_names)
print(f"Your customer Id is {user_id}.   NOTE:- Please remember this number as this maybe needed in future")


list_of_apparels = ['T-shirt', 'Shirt', 'Jacket']
list_of_sizes = ['Large', 'Medium', 'Small']
list_of_colour = ['Red', 'Blue', 'Green', 'Yellow', 'White']

apparel_type = """
    TYPE OF THE APPAREL:
    1. T-shirt.
    2. Shirt.
    3. Jacket.
    -->"""
apparel_size = """
    SIZE OF THE APPAREL:
    1. Large.
    2. Medium.
    3. Small.
    -->"""
apparel_colour = """
    COLOUR OF THE APPAREL:
    1. Red.
    2. Blue.
    3. Green.
    4. Yellow.
    5. White.
    -->"""


def type_of_apparel(number):
    return list_of_apparels[number - 1]


def size_of_apparel(number):
    return list_of_sizes[number - 1]


def colour_of_apparel(number):
    return list_of_colour[number - 1]


"""def purchase_cart():
    return cart


cart = {"Apparel Type": 0, "Apparel Size": 0, "Apparel Colour": 0}
"""


def Purchase_Apparels():

    user_id = input("enter your user_id:-")
    apparel_type_user_input = int(input(apparel_type))
    apparel_size_user_input = int(input(apparel_size))
    apparel_colour_user_input = int(input(apparel_colour))
    database.add_apparel_to_cart(user_id,apparel_type, apparel_size, apparel_colour)
    print("ITEM ADDED TO CART SUCCESSFULLY")

def payment_method():
    payment_method = """
    enter the method no. you would like to pay:-
    1) Net Banking
    2) Debit/Credit Card
    3) Cash
    ->"""
    payment_type = int(input(payment_method))
    key1 = Fernet(Fernet.generate_key())
    Key2 = Fernet(Fernet.generate_key())
    f = MultiFernet([key1, Key2])

    token = f.encrypt(payment_type)

    print(token)

    d = f.decrypt(token)

    print(d.decode())

user_input_menu = int(input(main_menu))

while user_input_menu != 5:

    if user_input_menu == 1:
        Purchase_Apparels()
    elif user_input_menu == 2:
        from trousers import trousers_function
        print(trousers_function())
    elif user_input_menu == 3:
        from shoes import shoes_function
        print(shoes_function())
    elif user_input_menu == 4:

        print("work is still going on..")

    else:
        print("Invalid Input Please Try Again!!!")
    user_input_menu = int(input(main_menu))
else:
    payment_method()
    print("Exiting the program...")
    print("Thank you...Have A Nice Day!!!")