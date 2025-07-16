from cryptography.fernet import Fernet
import os

# Resolve relative path to secure_store folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECURE_FOLDER = os.path.join(BASE_DIR, "secure_store")


def load_key():
    key_path = os.path.join(SECURE_FOLDER, "secret.key")
    with open(key_path, "rb") as key_file:
        return key_file.read()


def load_encrypted_properties(file_path=None):
    if not file_path:
        file_path = os.path.join(SECURE_FOLDER, "credentials.properties")

    props = {}
    with open(file_path, "r") as f:
        for line in f:
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.strip().split("=", 1)
                props[k.strip()] = v.strip()
    return props


def get_decrypted_credentials():
    key = load_key()
    fernet = Fernet(key)

    encrypted_props = load_encrypted_properties()
    decrypted = {
        k: fernet.decrypt(v.encode()).decode() for k, v in encrypted_props.items()
    }
    return decrypted
