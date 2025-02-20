from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase
from decouple import config
from initstorage import *
from register_user import *


class AnswerStore:
    def __int__(self, name, uid=None, qid=None, answer=None, weight=None):
        self.uid = uid
        self.qid = qid
        self.answer = answer
        self.weight = weight
        self.name = name

    def store_answer(self, uid, qid, answer, weight):
        url = config('url')
        engine = create_engine(url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        answer = AnswerData(uid=self.uid, qid=self.qid, answer=self.answer, weight=self.weight)
        session.add(answer)
        session.commit()
