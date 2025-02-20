from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON, select
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase
from decouple import config
from decouple import config
from initstorage import *


class User:
    def __init__(self, uid=None, name=None, password=None, age=None, gender=None):
        self.uid = uid
        self.name = name
        self.password = password
        self.age = age
        self.gender = gender

    def new_user(self):
        print('Hello new user.\nWhat is your name?')
        name = input('name: ')
        self.name = name
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
        self.password = password
        print("What is your age?")
        age = input('Age : ')
        self.age = age
        print("What is your gender, Male or Female?")
        while True:
            gender_options = ["Male", "male", "Female", "female"]
            gender = input("Gender : ")
            if gender not in gender_options:
                return True
            else:
                break
        self.gender = gender
        url = config('url')
        engine = create_engine(url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        name = input('please enter your name')
        stmt = select(UserData).where(UserData.name.in_([name]))
        for row in session.scalars(stmt):
            print(row.uid)
            self.uid = row.uid

    def identify_user(self):
        url = config('url')
        engine = create_engine(url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        name = input('please enter your name')
        stmt = select(UserData).where(UserData.name.in_([name]))
        for row in session.scalars(stmt):
            print(row.uid)

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
            user = User()
            User.new_user(user)
        else:
            user = User()
            User.identify_user(user)

    def __repr__(self):
        return self.name, self.password, self.age, self.gender, self.uid
