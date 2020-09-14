"""
Project: apparel shop test 2.
Author:Devam A

Description:shoes shop program is created and by making few change it can be added to the shop
status: success
stock: it needs database so this feature will be added later
"""






    user_input = 1
    while user_input != 3:

        user_input = int(input(main_menu))
        if user_input == 1:

        elif user_input == 2:
            print(f" you have selected {cart['Apparel Type']} apparel of size {cart['Apparel Size']} with {cart['Apparel Colour']} colour")
    else:
        print("GOING BACK TO MANI MENU.")
