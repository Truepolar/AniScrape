from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, insert
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase, Session
from decouple import config
from initstorage import *


class QuestionStore:
    def __init__(self, question, options):
        self.question = question
        self.options = options

    def store_question(self):
        url = config('url')
        engine = create_engine(url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        question = QuestionData(question=self.question, options=self.options)

        session.add(question)
        session.commit()


q1 = QuestionStore("1.Political alignment", {"a": "a.Left",
                                             "b": "b.Right"})
q2 = QuestionStore("2.Gender", {"a": "a.Male,",
                                "b": "b.Female"})
q3 = QuestionStore("3.Monthly income", {"a": "a.0-3k",
                                        "b": "b.3k-5k",
                                        "c": "c.5k-8k",
                                        "d": "d.8k-12k",
                                        "e": "e.12k and above",
                                        "f": "f.Does not matter"})
q4 = QuestionStore("4.Height in cm", {"a": "a.140-150",
                                      "b": "b.150-160",
                                      "c": "c.160-170",
                                      "d": "d.170-180",
                                      "e": "e.180 and above",
                                      "f": "f.Does not matter"})
q5 = QuestionStore("5.interests", {"a": "a.Reading",
                                   "b": "b.Music",
                                   "c": "c.Making music",
                                   "d": "d.Gaming",
                                   "e": "e.Sports",
                                   "f": "f.Food",
                                   "g": "g.others"})

all_questions = [q1, q2, q3, q4, q5]
for q in all_questions:
    q.store_question()
