from create_engine import *
from initstorage import UserData, AnswerData
from sqlalchemy import select, join


class CompareResults:
    def __init__(self):
        pass

    @staticmethod
    def compare(uid):
        ask_gender = input("Are you looking for Male or Females, type 'male' for males and 'female' for females")
        with get_session() as sess:
            stmt = select(UserData, AnswerData).join(AnswerData, UserData.uid == AnswerData.user_id).where(
                UserData.uid == uid, AnswerData.weight == 0)
            for row in sess.scalars(stmt):
                first_question = row.userl.question_id
                first_answer = row.userl.answer

        with get_session() as sess:
            stmt = select(UserData, AnswerData).join(AnswerData, UserData.uid == AnswerData.user_id).where(
                AnswerData.weight == 0, AnswerData.question_id == first_question, AnswerData.answer == first_answer, UserData.gender == ask_gender)
            list_of_users_1 = []
            list_of_users_email_1 = []
            for row in sess.scalars(stmt):
                list_of_users_1.append(row.name)
                list_of_users_email_1.append(row.email)


        with get_session() as sess:
            stmt = select(UserData, AnswerData).join(AnswerData, UserData.uid == AnswerData.user_id).where(
                AnswerData.weight == 1, AnswerData.question_id == first_question, AnswerData.answer == first_answer, UserData.gender == ask_gender)
            list_of_users_2 = []
            list_of_users_email_2 = []
            for row in sess.scalars(stmt):
                list_of_users_2.append(row.name)
                list_of_users_email_2.append(row.email)

        print("Best set of matches")

        print(list_of_users_1)
        print(list_of_users_email_1)

        print("\nNext best set of matches")

        print(list_of_users_2)
        print(list_of_users_email_2)
