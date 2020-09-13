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

        cursor.execute('CREATE TABLE IF NOT EXISTS cart(user_id integer primary key)')


def add_to_cart():
    with DatabaseConnection('Cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('')