from cryptography.fernet import Fernet
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECURE_FOLDER = os.path.join(BASE_DIR, "secure_store")

def load_key():
    key_path = os.path.join(SECURE_FOLDER, "secret.key")
    with open(key_path, "rb") as key_file:
        return key_file.read()

# Load key from file
key = load_key()

fernet = Fernet(key)

email = "your email address"
password = "your password here"

enc_email = fernet.encrypt(email.encode()).decode()
enc_password = fernet.encrypt(password.encode()).decode()

# Write encrypted credentials to credentials.properties
credentials_path = os.path.join(SECURE_FOLDER, "credentials.properties")
with open(credentials_path, "w") as f:
    f.write(f"instahyre_email={enc_email}\n")
    f.write(f"instahyre_password={enc_password}\n")

print(f"Encrypted credentials written to: {credentials_path}")