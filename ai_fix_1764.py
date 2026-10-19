import bcrypt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
users = db['users']

# Function to hash password
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

# Function to authenticate user
def authenticate(username, password):
    user = users.find_one({'username': username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return user
    return None

# Example usage
if __name__ == "__main__":
    # Hash a password
    password = "secure_password123"
    hashed_password = hash_password(password)
    print("Hashed Password:", hashed_password)

    # Insert a user
    user = {
        'username': 'admin',
        'password': hashed_password
    }
    users.insert_one(user)
    print("User inserted successfully")

    # Authenticate a user
    authenticated_user = authenticate('admin', 'secure_password123')
    if authenticated_user:
        print("Authentication successful:", authenticated_user)
    else:
        print("Authentication failed")