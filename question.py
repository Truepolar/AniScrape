from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase
from decouple import config

from initstorage import QuestionData

u1 = []
w1 = []


class Question():
    def __init__(self, question, options, check):
        self.question = question
        self.options = options
        self.check = check

        if ans not in check.key():
            return False
        return True

    # def askquestion(self):
    #     print(self.question)
    #     print(self.options)

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
                    print('dumbass')
            print('\n-------------------------------------')



