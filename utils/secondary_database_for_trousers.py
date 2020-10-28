"""
Project:secondary database for trouser.
Author: Devam A

Description:Create db for trousers and connect this with primary db
"""

from .database_connection import DatabaseConnection

def create_trouser_cart():
    with DatabaseConnection('Trouser_cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS Trousers(trouser_type text primary key, trouser_size text, trouser_colour text)')


def add_trouser_cart(trouser_type, trouser_size, trouser_colour):
    with DatabaseConnection('Trouser_cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Trouser VALUES(?,?,?)',(trouser_type, trouser_size, trouser_colour))

def view_trouser_cart():
    with DatabaseConnection('Trouser_cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Trouser')

        Trouser = [{'trouser_type': row[0], 'trouser_size': row[1], 'trouser_colour': row[2]} for row in cursor.fetchall()]
        return  Trouser



def remove_trouser_cart(trouser_type):
    with DatabaseConnection('Trouser_cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM Trouser WHERE trouser_type = ?',(trouser_type,))