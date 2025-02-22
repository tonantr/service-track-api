import logging
import jwt
import os
import datetime
from bcrypt import hashpw, gensalt, checkpw
from app.utils.helpers import Helpers

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - Line: %(lineno)d - %(message)s",
)


SECRET_KEY = os.getenv("FLASK_SECRET_KEY")


def hash_password(password):
    salt = gensalt()
    hashed_password = hashpw(password.encode(), salt)
    return hashed_password.decode("utf-8")


def verify_password(password, hashed_password):
    return checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


def is_password_plaintext(password):
    return len(password) < 60


def generate_token(username, user_id, role):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    payload = {
        "username": username,
        "user_id": user_id,   
        "role": role,         
        "exp": expiration     
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    return token


def authenticate(username, password, helpers: Helpers):
    try:
        user = helpers.get_user_by_username(username)

        if user:
            stored_password = user["password"]
            if is_password_plaintext(stored_password):
                hashed_password = hash_password(stored_password)
                helpers.update_password(username, hashed_password)
                stored_password = hashed_password

            if verify_password(password, stored_password):
                access_token = generate_token(username, user["user_id"], user["role"])
                return True, access_token if access_token else (False, None)
            else:
                return False, None
        else:
            return False, None
    except Exception as e:
        logging.error(f"Error in authenticate: {e}")
        print("\nAn error occurred while authenticating.")
        return False, None 
