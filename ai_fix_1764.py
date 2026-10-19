import bcrypt

def validate_input(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings")

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def sanitize_query(query):
    valid_fields = {"username", "password"}
    valid_operators = {"$eq", "$ne"}
    for key, value in query.items():
        if key not in valid_fields or (isinstance(value, dict) and "$ne" in value and list(value.keys())[0] not in valid_fields):
            raise ValueError("Invalid query structure")

def authenticate(username, password):
    validate_input(username, password)
    user = get_user_from_db(username)
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return user
    return None

def get_user_from_db(username):
    # Mock function to simulate database retrieval
    return {"username": username, "password": hash_password("securepassword")}