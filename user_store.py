from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase, Session
from decouple import config
from create_engine import get_session
from initstorage import *



class UserStore:

    @staticmethod
    def store_user(user):
        with get_session() as sess:
            sess.add(user)
            sess.commit()
