import bcrypt
from pymongo import MongoClient

def validate_input(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings")
    return username, password

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def authenticate(username, password):
    username, password = validate_input(username, password)
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database']
    collection = db['users']
    user = collection.find_one({"username": username, "password": password})
    return user

# Example usage
if __name__ == "__main__":
    username = "admin"
    password = "secure_password123"
    hashed_password = hash_password(password)
    user = authenticate(username, hashed_password)
    print(user)