import os
from cryptography.fernet import Fernet

def get_fernet():
    key = os.getenv('FERNET_KEY')
    return Fernet(key.encode())

def decrypt(value: str)->str:
    return get_fernet().decrypt(value.encode()).decode()