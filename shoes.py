"""
Project:Shoes
Author:Devam A

Description:shoes shop program is created and by making few change it can be added to the shop
status: success
"""
def shoes_function():
    list_of_shoes = ['Sports', 'Sneakers', 'Formal']
    list_of_sizes = ['12', '11', '10', '9', '8']
    list_of_colours = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Black', 'White']

    menu = """
    1. add shoes to the cart
    2. view the cart
    3. exit the program
    -->"""

    shoes_type_menu = """
    Select the type of shoes you ant to purchase:
    1. Sports
    2. Sneakers
    3. Formal
    -->"""

    shoes_size_menu = """
    Select the size of shoes
    1. 12
    2. 11
    3. 10
    4. 9
    5. 8
    -->"""

    shoes_colour_menu = """
    1. Red
    2. Blue
    3. Green
    4. Yellow
    5. Orange
    6. Black
    7. White
    -->"""
    cart = {"Shoes Type":0, "Shoes Size":0, "Shoes Colour":0}

    def shoes_type(option):
        return list_of_shoes[option - 1]
    def shoes_size(option):
        return list_of_sizes[option - 1]
    def shoes_colour(option):
        return list_of_colours[option - 1]

    user_input = 1
    while user_input != 3:
        user_input = int(input(menu))
        if user_input == 1:
            shoes_type_user_input = int(input(shoes_type_menu))
            value = shoes_type(shoes_type_user_input)
            cart["Shoes Type"] = value

            shoes_size_user_input = int(input(shoes_size_menu))
            value = shoes_size(shoes_size_user_input)
            cart["Shoes Size"] = value

            shoes_colour_user_input = int(input(shoes_colour_menu))
            value = shoes_colour(shoes_colour_user_input)
            cart["Shoes Colour"] = value
            print("SHOES ADD TO CART SUCCESSFULY!!")
        elif user_input == 2:
            print(f"you have selected {cart['Shoes Type']} type shoes of {cart['Shoes Size']} size with {cart['Shoes Colour']} colour")

    else:
        print("THANK YOU !!! COME AGAIN...")