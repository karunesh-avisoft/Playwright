import os
from utilities.crypto_utils import decrypt
from utilities.test_data import TestData as TD

def get_user(user_key: str):
    encrypted = TD.ENCRYPTED_USERS
    return decrypt(encrypted.get(user_key))

def get_passwd():
    return decrypt(TD.ENCRYPTED_PASSWD)     