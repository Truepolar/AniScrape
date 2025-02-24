from sqlalchemy import update
from initstorage import *
from question import *
from create_engine import *


class AnswerStore:

    @staticmethod
    def store_answer(ans):
        with get_session() as sess:
            sess.add(ans)
            sess.commit()

    @staticmethod
    def store_weight(uid,weight):
        for i in range(0, 5):
            val = weight[i]
            with get_session() as sess:
                stmt = update(AnswerData).where(AnswerData.question_id == val, AnswerData.user_id == uid).values(weight=i)
                sess.add(stmt)
                sess.commit()
