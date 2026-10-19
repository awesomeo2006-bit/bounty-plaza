import bcrypt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
users = db['users']

def validate_input(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Invalid input types")
    return username, password

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def authenticate(username, password):
    validated_username, validated_password = validate_input(username, password)
    hashed_password = hash_password(validated_password)

    user = users.find_one({"username": validated_username, "password": hashed_password})
    if user:
        return user
    else:
        return None

# Example usage
# user = authenticate("admin", "password123")
# print(user)