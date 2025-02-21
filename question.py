from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase
from decouple import config
from answer_store import *
from initstorage import QuestionData

u1 = []
w1 = []


class Question():
    def __init__(self, answer=None,weight=None):
        self.answer = answer
        self.weight = weight

    @staticmethod
    def askquestion():
        url = config('url')
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        session = Session()
        stmt = select(QuestionData)

        for row in session.scalars(stmt):
            print(row.question, "\n")
            for key in row.options:
                row.options[key] += ""
            for value in row.options.values():
                print(value)
            while True:
                val = input()

                gate = [*row.options.keys()]
                if val in gate:
                    print('very cool')
                    break
                else:
                    print('dumb ass')
            print('\n-------------------------------------')
            AnswerStore.store_answer()



    @staticmethod
    def askweight():
        url = config('url')
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        session = Session()
        stmt = select(QuestionData)
        print("Please rank the questions in order of most important to least important")
        for row in session.scalars(stmt):
            print(*row.question)
        gate = []
        for row in session.scalars(stmt):
            gate.append(str(row.qid))
        print(gate)
        while True:
            val = input("eg. 2,3,4,5,1\n").split(",")
            sorted_val = sorted(val)
            print(sorted_val)
            if sorted_val == gate:
                print("very interesting")
                break
            else:
                print("wtf are you doing?")

    def __repr__(self):
        return self.answer, self.weight
