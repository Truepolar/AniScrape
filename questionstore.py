from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, insert
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase, Session
from decouple import config
from initstorage import *


class Qstore:
    def __init__(self, question, options, checks, answer=None):
        self.question = question
        self.options = options
        self.checks = checks
        self.answer = answer

    def storeq(self, question, options, checks):
        url = config('url')
        engine = create_engine(url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        question = QuestionS(question=self.question, options=self.options, checks=self.checks)

        session.add(question)
        session.commit()


q1 = Qstore("1.Political alignment", " a.Left \n b.Right", {"a", "b"}, 0)
q2 = Qstore("2.Gender", " a.Male\n b.Female", {"a", "b"}, 0)
q3 = Qstore("3.Monthly income", "a.0-3k \n b.3k-5k \n c.5k-8k \n d.8k-12k \n e.12k and above \n f.Does not matter",
            {"a", "b", "c", "d", "e", "f"}, 0)
q4 = Qstore("4.Height in cm",
            "a.140-150 \n b.150-160 \n c.160-170 \n d.170-180 \n e.180 and above \n f.Does not matter",
            {"a", "b", "c", "d", "e", "f"}, 0)
q5 = Qstore("5.interests", "a.Reading \n b.Music \n c.Making music \n d.Gaming \n e.Sports \n f.Food \n g.others",
            {"a", "b", "c", "d", "e", "f", "g"}, 0)

all_questions = [q1, q2, q3, q4, q5]
for q in all_questions:
    q.storeq()
