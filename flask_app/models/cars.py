from flask_app.config.dbconnect import connectToMySQL
from flask import flash
from flask_app.models.users import User
import re
class Car:
    def __init__(self, data):
        self.id = data["id"]
        self.make = data["make"]
        self.model = data["model"]
        self.price = data["price"]
        self.year = data["year"]
        self.isPurchased = data["isPurchased"]
        self.description = data["description"]
        self.created_date = data["created_date"]
        self.updated_date = data["updated_date"]
        self.user_id = data["user_id"]
        self.poster=None
        self.buyer=None

       

    @staticmethod
    def validate_car(data):
        is_valid = True
        year = data["year"]
        price = data["price"]

        if int(year) <= 0:
            flash("There weren't any cars in year zero")
            is_valid= False
        if int(price) <= 0:
            flash("you can't give away cars")
            is_valid= False
      
        return is_valid
        
        
        

    @classmethod
    def login_with_email(cls,data):
        query = "SELECT * from users WHERE email=%(email)s"

        

        results = connectToMySQL("carsDB").query_db(query,data)
        

        if len(results)<1:
            return False
        return cls(results[0])

    @classmethod
    def get_cars(cls):
        query = "SELECT * from cars JOIN carsDB.users ON carsDB.users.id = user_id"

        

        results = connectToMySQL("carsDB").query_db(query)
        cars = []

        for car in results:
            this_car = cls(car)
            poster = {
            "id":car["users.id"],
            "first_name":car["first_name"],
            "last_name":car["last_name"],
            "email":car["email"],
            "password":None,
            "created_date":car["created_date"],
            "updated_date":car["updated_date"],
            
            
        }
            this_car.poster=User(poster)
            cars.append(this_car)
            
        return cars
    @classmethod
    def get_one_car_by_id(cls, data):
        query = "SELECT * from cars WHERE id=%(id)s"


        results = connectToMySQL("carsDB").query_db(query, data)

        if len(results) < 1:
            return False
        return cls(results[0])
    @classmethod
    def display_car_with_poster(cls, data):
        query = "SELECT * from cars JOIN carsDB.users ON carsDB.users.id = user_id WHERE cars.id=%(id)s"

        # SELECT * from recipes
        # JOIN carsDB.users ON carsDB.users.id = user_id
        # WHERE recipes.user_id = 5

        
        results = connectToMySQL("carsDB").query_db(query, data)
        #change to car items
        for item in results:
            car = Car(item)
            poster = {
            "id":item["users.id"],
            "first_name":item["first_name"],
            "last_name":item["last_name"],
            "email":item["email"],
            "password":None,
            "created_date":item["created_date"],
            "updated_date":item["updated_date"],
            
            
        }
        car.poster=User(poster)
        
        
        if len(results) < 1:
            return False
        return car

    @classmethod
    def create_car(cls,data):
        query = "INSERT INTO cars (make,model,price,year,isPurchased,description,updated_date,created_date,user_id) VALUES(%(make)s,%(model)s,%(price)s,%(year)s,%(isPurchased)s,%(description)s,NOW(),NOW(),%(user_id)s)"
                  

        return connectToMySQL("carsDB").query_db(query,data)
    @classmethod
    def edit_car(cls,data):
        query = "UPDATE cars SET make=%(make)s,model=%(model)s,price=%(price)s,year=%(year)s,description=%(description)s,updated_date=NOW() WHERE cars.id=%(id)s"
                  

        return connectToMySQL("carsDB").query_db(query,data)
    @classmethod
    def purchase_car(cls,data):
        query = "UPDATE cars SET isPurchased=1,buyer_id=%(id)s WHERE cars.id=%(car_id)s"
                  

        return connectToMySQL("carsDB").query_db(query,data)
        
        
    @classmethod
    def del_car(cls,data):
        query = "DELETE FROM cars WHERE id=%(id)s;"

        return connectToMySQL("carsDB").query_db(query,data)

    @classmethod
    def show_cars_with_user(cls, data):
        query = "SELECT * from cars JOIN carsDB.users ON carsDB.users.id = buyer_id WHERE buyer_id=%(id)s"
        results = connectToMySQL("carsDB").query_db(query,data)

        for item in results:
            cls(item)
        return results
        



