from sqlalchemy import update, values
from sqlalchemy.orm import query
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
    def store_weight(uid, weight):
        for i in range(0, 5):
            val = weight[i]
            with get_session() as sess:
                stmt = update(AnswerData).where(AnswerData.user_id == uid, AnswerData.question_id == val).values(
                    weight=i)
                sess.execute(stmt)
                sess.commit()