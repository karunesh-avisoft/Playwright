import os
from utilities.crypto_utils import decrypt

def get_users():
    encrypted = os.getenv("ENCRYPTED_USERS").split(",")
    return [decrypt(user) for user in encrypted]

def get_passwd():
    return decrypt(os.getenv("ENCRYPTED_PASSWD"))