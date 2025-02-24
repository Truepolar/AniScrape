from sqlalchemy import select
from answer_store import *
from initstorage import QuestionData
from create_engine import *

u1 = []
w1 = []


class Question():
    # def __init__(self, answer=None, weight=None, uid=None):

    @staticmethod
    def askquestion(uid):
        with get_session() as sess:
            stmt = select(QuestionData)

            for row in sess.scalars(stmt):
                ans = AnswerData()
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
                ans.user_id = uid
                ans.question_id = row.qid
                ans.answer = val
                AnswerStore.store_answer(ans)

    @staticmethod
    def askweight(uid):
        with get_session() as sess:
            stmt = select(QuestionData)
            print("Please rank the questions in order of most important to least important")
            for row in sess.scalars(stmt):
                print(*row.question)
            gate = []
            for row in sess.scalars(stmt):
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

            AnswerStore.store_weight(uid, val)
