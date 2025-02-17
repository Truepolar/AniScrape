from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, insert
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase, Session
from decouple import config
from initstorage import *


class Qstore:
    def __init__(self, question, options):
        self.question = question
        self.options = options

    def storeq(self):
        url = config('url')
        engine = create_engine(url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        question = QuestionS(question=self.question, options=self.options)

        session.add(question)
        session.commit()


q1 = Qstore("1.Political alignment", {" a": ".Left",
                                      "b": ".Right"})
q2 = Qstore("2.Gender", {" a": ".Male,",
                         "b": ".Female"})
q3 = Qstore("3.Monthly income", {"a": ".0-3k",
                                 "b": ".3k-5k",
                                 "c": ".5k-8k",
                                 "d": ".8k-12k",
                                 "e": ".12k and above",
                                 "f": ".Does not matter"})
q4 = Qstore("4.Height in cm", {"a": ".140-150",
                               "b": ".150-160",
                               "c": ".160-170",
                               "d": ".170-180",
                               "e": ".180 and above",
                               "f": ".Does not matter"})
q5 = Qstore("5.interests", {"a": ".Reading",
                            "b": ".Music",
                            "c": ".Making music",
                            "d": ".Gaming",
                            "e": ".Sports",
                            "f": ".Food",
                            "g": ".others"})

all_questions = [q1, q2, q3, q4, q5]
for q in all_questions:
    q.storeq()
