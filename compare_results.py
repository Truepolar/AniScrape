from create_engine import *
from initstorage import UserData, AnswerData
from sqlalchemy import select

class CompareResults:
    def __init__(self):
        pass

    @staticmethod
    def compare(uid):
        with get_session() as sess:
            stmt = select(UserData, AnswerData).join(UserData.uid).where(UserData.uid == uid, AnswerData.weight == 0)
            question_priority = stmt.user_id
            print(question_priority)


CompareResults.compare(1)