import logging
from app.database.database_handler import DatabaseHandler
from app.utils.constants import ERROR_PLEASE_LOG_IN
from flask import flash, session


logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - Line: %(lineno)d - %(message)s",
)


class Helpers:
    def __init__(self, db_handler: DatabaseHandler):
        self.db_handler = db_handler

    def get_user_by_username(self, username):
        try:
            query = "SELECT * FROM users WHERE username = %s"
            with self.db_handler as db:
                return db.fetch_one(query, (username,))
        except Exception as e:
            logging.error(f"Error in get_user_by_username: {e}")
            raise Exception(f"An error occurred while loading the user: {str(e)}")

    def update_password(self, username, hashed_password):
        try:
            query = "UPDATE users SET password = %s WHERE username = %s"
            with self.db_handler as db:
                db.execute_commit(query, (hashed_password, username))
        except Exception as e:
            logging.error(f"Error in check_vin_exists: {e}")
            raise Exception(f"An error occurred while checking the vin: {str(e)}")
