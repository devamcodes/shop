"""
Project:
Author:Devam A

Description:By importing the three shop functions in this file and changing few lines a proper shop program is created
status:ongoing.
"""

from utils import database

main_menu = """
1. Purchase Apparels
2. Purchase Trousers
3. Purchase Shoes
4. View Cart
5. Exit The Program
"""
#todo: exit program option needed.
My_cart = [
    {'Apparel': 'Apparel Type', "Size": 'Apparel Size', "Colour": 'Apparel Colour'},
]

user_names = []
user_name = input("enter your name:-")
user_name_bool = bool(user_name)
if user_name_bool:
    print(f"Welcome!! To the cloths shop, {user_name.title()}")

else:
    raise ValueError("Invalid Name!! Please try again...")

user_names.append(user_name)
user_id = len(user_names)
print(f"Your customer Id is {user_id}.NOTE:- Please remember this number as this maybe needed in future")

def 

user_input_menu = int(input(main_menu))

while user_input_menu != 5:

    if user_input_menu == 1:
        from Apparels import apparels_function
        print(apparels_function())
    elif user_input_menu == 2:
        from trousers import trousers_function
        print(trousers_function())
    elif user_input_menu == 3:
        from shoes import shoes_function
        print(shoes_function())
    elif user_input_menu == 4:
        print(My_cart)
        print("work is still going on..")

    else:
        print("Invalid Input Please Try Again!!!")
    user_input_menu = int(input(main_menu))
else:
    print("Exiting the program...")
    print("Thank you...Have A Nice Day!!!")

