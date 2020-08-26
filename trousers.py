"""
Project:Trousers
Author:Devam A
Description: trouser shop program is created and by making few change it can be added to the shop
"""
def trousers_function():
    list_of_trousers = ['Jeans', 'Formal', 'Cotton Based', 'Cargo']
    list_of_sizes = ['Large', 'Medium', 'Small']
    list_of_colours = ['Yellow', 'Black', 'Blue',]

    menu = """
    1. ADD TROUSER TP THE CART
    2. VIEW THE CART
    3. EXIT THE PROGRAM
    -->"""

    trouser_type_menu = """
    1. Jeans
    2. Formal
    3. Cotton Based
    4. Cargo
    -->"""

    trouser_size_menu = """
    1. Large
    2. Medium
    3. Small
    -->"""

    trouser_colour_menu = """
    1. Yellow
    2. Black
    3. Blue
    -->"""

    def trouser_type(option):
        return list_of_trousers[option - 1]
    def trouser_size(option):
        return list_of_sizes[option - 1]
    def trouser_colour(option):
        return list_of_colours[option - 1]

    cart = {"Trouser Type":0, "Trouser Size":0, "Trouser Colour":0}
    user_input = 1
    while user_input != 3:
        user_input = int(input(menu))
        if user_input == 1:
            trouser_type_user_input = int(input(trouser_type_menu))
            value = trouser_type(trouser_type_user_input)
            cart["Trouser Type"] = value

            trouser_size_user_input = int(input(trouser_size_menu))
            value = trouser_size(trouser_size_user_input)
            cart["Trouser Size"] = value

            trouser_colour_user_input = int(input(trouser_colour_menu))
            value = trouser_colour(trouser_colour_user_input)
            cart["Trouser Colour"] = value
        elif user_input == 2:
            print(f"you have selected {cart['Trouser Type']} type trouser with {cart['Trouser Size']} size and {cart['Trouser Colour']} colour")
    else:
        print(" THANK YOU !!! COME AGAIN..")