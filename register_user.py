from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON, select
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase
from decouple import config
from decouple import config
from initstorage import *
from create_engine import get_session
from user_store import *

class RegisterUser:
    def __init__(self, uid=None, name=None, password=None, age=None, gender=None):
        self.uid = uid
        self.name = name
        self.password = password
        self.age = age
        self.gender = gender

    @staticmethod
    def new_user():
        print('Hello new user.\nWhat is your name?')
        user = UserData()
        name = input('name: ')
        user.name = name
        print("Hello " + name)
        while True:
            confirm = 'no'
            print("Please enter a password")
            password = input("Password : ")
            print("Please enter password again")
            confirm = input("Password : ")
            if password == confirm:
                break
            else:
                print("Passwords do not match. \nPlease try again")
        user.password = password
        print("What is your age?")
        age = input('Age : ')
        user.age = age
        print("What is your gender, Male or Female?")
        while True:
            gender_options = ["Male", "male", "Female", "female"]
            gender = input("Gender : ")
            if gender not in gender_options:
                return True
            else:
                break
        user.gender = gender
        print("Please input your email\nDo not reuse the same email\n")
        email = input()
        user.email = email
        UserStore.store_user(user)

    @staticmethod
    def initial_page():
        while True:
            print("Type n for new user and l for login")
            gate = ['n', 'l']
            val = input()
            if val in gate:
                break
            else:
                print("Please try again")

        if val == "n":
            RegisterUser.new_user()
        else:
            pass
    def __repr__(self):
        return self.name, self.password, self.age, self.gender, self.uid

