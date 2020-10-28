"""
Project: encryption.
Author:Devam A

Description: This project is test project for encryption and decryption which can be added into shop project.
Status: Learning.
"""

from cryptography.fernet import Fernet, MultiFernet

key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())

f = MultiFernet([key1, key2])

token = f.encrypt(b"My name is Devam Agrawal.")

print(token)

d = f.decrypt(token)

print(d.decode())

name = input("enter your name:-")
address = input("enter your address:-")
