"""
Project: Database for project shop.
Author: Devam A

Description: create stock, create cart.

"""
"""
create stock so that shop owner can have all the record for all the items 
if any customer purchases any item from him he needs to update the database as well as create a bill for the customer.
so you can create another database for the customer to purchase something or find a way to combine both the process 
and do them simultaneously. 

"""
from .database_connection import DatabaseConnection

def create_cart():
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS Cart(user_id integer primary key, apparel_type text, apparel_size text, apparel_colour text, trouser_type text, trouser_size text, trouser-colour text, shoes_type text, shoes_size text, shoes_colour text)')


def add_apparel_to_cart(user_id, apparel_type, apparel_size, apparel_colour):
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Cart VALUES(?,?,?,?,?,?,?,?,?,?)',(user_id, apparel_type, apparel_size, apparel_colour))


def add_trouser_to_cart(user_id, trouser_type, trouser_size, trouser_colour):
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Cart VALUES(?,?,?,?',(user_id, trouser_type, trouser_size, trouser_colour))


def add_shoes_to_cart(user_id, shoes_type, shoes_size, shoes_colour):
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Cart VALUES(?,?,?,?)', (user_id, shoes_type, shoes_size, shoes_colour))

def view_cart():
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Cart')

        Cart = [{"user Id":row[0], "Apparel Type":row[1], "Apparel Size":row[2], "Apparel Colour":row[3], "Trouser Type":row[4], "Trouser Size":row[5], "Trouser Colour":row[6], "Shoes Type":row[7], "Shoes Size":row[8], "Shoes Colour":row[9]} for row in cursor.fetchall()]
        return  Cart


def view_apparels_in_cart():
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Cart')

        Cart = [{"user Id": row[0], "Apparel Type": row[1], "Apparel Size": row[2], "Apparel Colour": row[3]} for row in cursor.fetchall()]
        return Cart


def view_trouser_in_cart():
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Cart')

        Cart = [{"user Id": row[0], "Trouser Type": row[4], "Trouser Size": row[5], "Trouser Colour": row[6]} for row in cursor.fetchall()]
        return Cart


def view_shoes_in_cart():
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Cart')

        Cart = [{"user Id": row[0], "Shoes Type": row[7], "Shoes Size": row[8], "Shoes Colour": row[9]} for row in cursor.fetchall()]
        return Cart

"""
def remove_from_cart(user_id):
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM Cart WHERE user_id = ?',(user_id,))

"""
def update_apparels_in_cart(user_id, apparel_type, apparel_size, apparel_colour):
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE Cart SET WHERE VALUES(?,?,?,?)',(user_id, apparel_type, apparel_size, apparel_colour))


def update_trousers_in_cart(user_id, trouser_type, trouser_size, trouser_colour):
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE Cart SET WHERE VALUES(?,?,?,?)',(user_id, trouser_type,trouser_size,trouser_colour))


def update_shoes_in_cart(user_id, shoes_type, shoes_size, shoes_colour):
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE Cart SET WHERE VALUES(?,?,?,?)',(user_id, shoes_type,shoes_size,shoes_colour))

