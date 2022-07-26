
from contextlib import redirect_stderr
from flask_app import app
from flask import render_template, session, redirect,request
from flask_app.models.users import User
from flask_app.models.cars import Car
from flask import flash


@app.route("/")
def index():
    
    user_list = User.get_users()
    return render_template("index.html",user_list=user_list)
@app.route("/create_car")
def create_car():
    if session["user_id"]:
        data = {
            "id":session["user_id"]
        }
    else:
        redirect("/")
    logged_user = User.get_one_user_by_id(data)

    



    return render_template("/create_car.html",user=logged_user)

@app.route("/edit_car/<int:id>")
def edit_car(id):

    data = {
        "id":id
    }
    car = Car.display_car_with_poster(data)
    data = {
        "id":session["user_id"]
    }
    session["id"] = car.id

    user = User.get_one_user_by_id(data)


    if user.id != car.poster.id:
        flash("you didn't make that car!")
        return redirect("/dashboard")


    



    return render_template("/edit_car.html", user=user,car=car)

@app.route("/post_car", methods=["POST"])
def post_car():

    
    car ={
        "user_id":session["user_id"],        
        "model":request.form["model"],
        "make":request.form["make"],
        "price":request.form["price"],
        "year":request.form["year"],
        "description":request.form["description"],
        "isPurchased":0,
        
        

    }
    if Car.validate_car(car)==True:
        Car.create_car(car)
    else:
        return redirect("/create_car")

    
    
    

    print(car)

    return redirect("/dashboard")
@app.route("/post_edit", methods=["POST"])
def post_edit():

    car ={
        "id":session["id"],
        "model":request.form["model"],
        "make":request.form["make"],
        "price":request.form["price"],
        "year":request.form["year"],
        "description":request.form["description"],

        

    }

    if Car.validate_car(car)==True:
        Car.edit_car(car)
    else:
        return redirect("/edit_car/"+str(session["id"]))
    
    del session["id"]
    

    return redirect("/dashboard")
@app.route("/delete_car/<int:id>")
def delete_car(id):
    data={
        "id":id
    }
    car = Car.display_car_with_poster(data)
    if session["user_id"] != car.poster.id:
        flash("you didn't make that car!")
        return redirect("/dashboard")
    else:
        data = {
            "id": car.id
        }
        car.del_car(data)
        return redirect("/dashboard")

@app.route("/view_car/<int:id>")
def view_car(id):
    data = {
        "id":id
            }
    session["car_id"]=id

    print(Car.display_car_with_poster(data))
    car = Car.display_car_with_poster(data)

    
    data = {
        "id":session["user_id"]
    }
    logged_user = User.get_one_user_by_id(data)
    




    return render_template("/view_car.html",id=id,user=logged_user,car=car)



@app.route("/dashboard")
def dashboard_view():
    if "user_id" not in session:
        flash("Please login before you try and view cars! :D")
        return redirect("/")
    else:
        data = {
            "id":session["user_id"],
            
        }
        logged_user = User.get_one_user_by_id(data)
 
        

    
    

    
    car_list = Car.get_cars()
    print(car_list)

    return render_template("dashboard.html",car_list = car_list,user=logged_user )

@app.route("/logout",methods=["POST"])
def logout():
    if session["user_id"]:
        del session["user_id"]

    return redirect("/")
@app.route("/buy_car")
def purchase_car():
    data={
        "id":session["user_id"],
        "car_id":session["car_id"]

    }
    Car.purchase_car(data)

    return redirect("/dashboard")
@app.route("/my_cars")
def display_owned_cars():
    if "user_id" not in session:
        flash("Please login before you try and view cars! :D")
        return redirect("/")
    else:
        data = {
            "id":session["user_id"]
        }
        logged_user = User.get_one_user_by_id(data)
 
    data={
        "id":session["user_id"]

    }
    car_list = Car.show_cars_with_user(data)

    return render_template("/my_cars.html",user=logged_user, car_list=car_list)