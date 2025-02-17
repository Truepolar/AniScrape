from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase
from decouple import config

u1 = []
w1 = []


class Question():
    def __init__(self, question, options, check, ):
        self.question = question
        self.options = options
        self.check = check

    def qchecker(self, ans):
        if ans not in self.check:
            return False
        return True

    def askquestion(self):
        print(self.question)
        print(self.options)

    def fullquestion(self):
        url = config('url')
        engine = create_engine(url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        for q in Question:
            q = select



