import secrets
import hashlib

def generate_api_key():
    return secrets.token_hex(16)

def hash_string(s: str):
    return hashlib.sha256(s.encode()).hexdigest()
