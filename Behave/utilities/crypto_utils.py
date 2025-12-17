from utilities.test_data import TestData as TD
from cryptography.fernet import Fernet

def get_fernet():
    key = TD.FERNET_KEY
    return Fernet(key.encode())

def decrypt(value: str)->str:
    return get_fernet().decrypt(value.encode()).decode()