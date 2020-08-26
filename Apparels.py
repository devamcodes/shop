"""
Project: apparel shop test 2.
Author:Devam A

Description:shoes shop program is created and by making few change it can be added to the shop
status: success
stock: it needs database so this feature will be added later
"""
def apparels_function():
    list_of_apparels = ['T-shirt', 'Shirt', 'Jacket']
    list_of_sizes = ['Large', 'Medium', 'Small']
    list_of_colour = ['Red', 'Blue', 'Green', 'Yellow', 'White']

    user_name = input("ENTER YOUR NAME:")
    print(f"WELCOME TO THE SHOP, Mr.{user_name.title()}.")
    main_menu = """
    SELECT ANY ONE OPTION FROM THE MENU:
    1. ADD APPAREL TO THE CART.
    2. VIEW THE CART.
    3. EXIT THE PROGRAM.
    -->"""
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
    def purchase_cart():
        return cart
    cart = {"Apparel Type":0, "Apparel Size":0, "Apparel Colour":0}
    user_input = 1
    while user_input != 3:

        user_input = int(input(main_menu))
        if user_input == 1:
            apparel_type_user_input = int(input(apparel_type))
            value = type_of_apparel(apparel_type_user_input)
            cart["Apparel Type"] = value
            apparel_size_user_input = int(input(apparel_size))
            value = size_of_apparel(apparel_size_user_input)
            cart["Apparel Size"] = value
            apparel_colour_user_input = int(input(apparel_colour))
            value = colour_of_apparel(apparel_colour_user_input)
            cart["Apparel Colour"] = value
            print("ITEM ADDED TO CART SUCCESSFULLY")
        elif user_input == 2:
            print(f" you have selected {cart['Apparel Type']} apparel of size {cart['Apparel Size']} with {cart['Apparel Colour']} colour")
    else:
        print("GOING BACK TO MANI MENU.")
