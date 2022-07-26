
import re
from flask_app import app
from flask import render_template,request,redirect,session
from flask_app.models.users import User
from flask_app.models.cars import Car
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt=Bcrypt(app)

# @app.route("/test", methods=["POST"])
# def test():
#     data={
#     "email":request.form["email"]
#     }
#     user = User.get_user_by_email(data)
#     print(user.first_name)
#     return "cool"
@app.route("/create_user", methods=["POST"])
def create_user():
    data={
    "email":request.form["email"]
    }
    existing_user = User.get_user_by_email(data)

    data={
    "first_name":request.form["first_name"],
    "last_name":request.form["last_name"],
    "email":request.form["email"],
    "password":request.form["password"],
    "confirm_password":request.form["confirm_password"]
   }
    if type(existing_user) != bool:
        if existing_user.email==request.form["email"]:
            flash("User Exists in Database")
            return redirect("/")

    if User.validate_user(data) == False:
        return redirect("/")

    else:
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data={
    "first_name":request.form["first_name"],
    "last_name":request.form["last_name"],
    "email":request.form["email"],
    "password":pw_hash
    
   }
        user_id=User.create_user(data)
        print(pw_hash)
        session["user_id"]=user_id
        print(session["user_id"])
   
    return redirect("/dashboard")
@app.route("/login", methods = ["POST"])
def login():

    data={
    "email":request.form["email"]
    }
    existing_user = User.get_user_by_email(data)
        
    if type(existing_user) != bool:
        if bcrypt.check_password_hash(existing_user.password,request.form["password"] ):
            session["user_id"] = existing_user.id
            return redirect("/dashboard")
    else:
        flash("Incorrect Login Information!")
        return redirect("/")