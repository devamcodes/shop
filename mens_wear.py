"""
Project:
Author:Devam A

Description:By importing the three shop functions in this file and changing few lines a proper shop program is created
status:ongoing.
"""
main_menu = """
1. Purchase Apparels
2. Purchase Trousers
3. Purchase Shoes
4. View Cart
"""
#todo: exit program option needed.
My_cart = [
    {'Apparel': 'Apparel Type', "Size": 'Apparel Size', "Colour": 'Apparel Colour'},




]
user_input_menu = int(input(main_menu))
#todo:after getting the error the loop should continue.
while user_input_menu != 4:
    user_input_menu = int(input(main_menu))#todo: this menu should be kept at the end to continue the program.
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