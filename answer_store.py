from sqlalchemy import create_engine, select, insert
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase
from decouple import config
from initstorage import *
from register_user import *
from create_engine import *


class AnswerStore:
    def __int__(self, name, aid=None, uid=None, qid=None, answer=None, weight=None):
        self.aid = aid
        self.uid = uid
        self.qid = qid
        self.answer = answer
        self.weight = weight
        self.name = name

    def store_answer(self):
        with get_session() as sess:
            answer = AnswerData(user_id=self.uid, question_id=self.qid, answer=self.answer)
            sess.add(answer)
            sess.commit()

    def store_weight(self, lst):
        for i in range(0, 5):
            val = lst.index(i)
            with get_session() as sess:
                stmt = AnswerData(weight=i),
                sess.add(stmt)
                sess.commit()
