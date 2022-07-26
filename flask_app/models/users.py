from flask_app.config.dbconnect import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt
# .{10} regex date


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_date = data["created_date"]
        self.updated_date = data["updated_date"]

    @staticmethod
    def validate_user(data):
        is_valid = True
        EMAIL_REGEX = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if len(data["first_name"])<3 or len(data["last_name"]) > 255:
            flash("your first name must be in between 3 and 255 characters")
            is_valid= False
        if len(data["last_name"])<3 or len(data["last_name"]) > 255:
            flash("your last name must be in between 3 and 255 characters")
            is_valid= False
        if data["password"] != data["confirm_password"]:
            flash("Your Passwords don't match you dingus")
            is_valid = False
        if len(data["password"]) < 8 :
            flash("Your Password must be at least 8 characters")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Please use da PROPA FO MAT for EMAIl")
            is_valid = False
        return is_valid

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * from users WHERE email=%(email)s"

        results = connectToMySQL("carsDB").query_db(query, data)

        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_one_user_by_id(cls, data):
        query = "SELECT * from users WHERE id=%(id)s"

        results = connectToMySQL("carsDB").query_db(query, data)

        if len(results) < 1:
            return False
        return cls(results[0])


    @classmethod
    def get_users(cls):
        query = "SELECT * from users"

        results = connectToMySQL("carsDB").query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_ninja(cls):
        pass

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,password,updated_date,created_date) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW())"

        return connectToMySQL("carsDB").query_db(query, data)

    @classmethod
    def del_ninja(cls):
        pass
