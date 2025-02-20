from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase, Session
from decouple import config
from initstorage import *
from register_user import *

class UserStore:

    def __init__(self):
        pass
    @staticmethod
    def store_user(user:User):
        url = config('url')
        engine = create_engine(url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        user = UserData(name=user.name, password=user.password, age=user.age, gender=user.gender)

        session.add(user)
        session.commit()


