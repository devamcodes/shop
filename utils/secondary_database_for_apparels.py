
from .database_connection import DatabaseConnection

def create_trouser_cart():
    with DatabaseConnection('Apparel_cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS Trousers(apparel_type text primary key, apparel_size text, apparel_colour text)')


def add_apparel_cart(apparel_type, apparel_size, apparel_colour):
    with DatabaseConnection('Apparel_cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Apparel VALUES(?,?,?)',(apparel_type, apparel_size, apparel_colour))

def view_apparel_cart():
    with DatabaseConnection('Apparel_cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Apparel')

        Apparel = [{'apparel_type': row[0], 'apparel_size': row[1], 'apparel_colour': row[2]} for row in cursor.fetchall()]
        return  Apparel



def remove_apparel_cart(apparel_type):
    with DatabaseConnection('Apparel_cart.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM Apparel WHERE apparel_type = ?',(apparel_type,))