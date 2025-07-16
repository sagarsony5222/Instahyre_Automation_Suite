import os
from cryptography.fernet import Fernet

SECURE_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "secure_store")
os.makedirs(SECURE_FOLDER, exist_ok=True)

key_path = os.path.join(SECURE_FOLDER, "secret.key")
key = Fernet.generate_key()

with open(key_path, "wb") as f:
    f.write(key)

print(f"Key generated and stored at: {key_path}")
