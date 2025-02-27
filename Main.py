from user_store import *
from question import *
from register_user import RegisterUser
from answer_store import AnswerStore
from compare_results import CompareResults

RegisterUser.initial_page()

# -------------------------------

with get_session() as sess:
    name = input('please enter your name')
    stmt = select(UserData).where(UserData.name.in_([name]))
    for row in sess.scalars(stmt):
        print(row.uid)
        uid = row.uid

# -------------------------------

while True:
    print("type 'c' to check results and type 'a' to answer the questions")
    val = input()
    gate = ["a","c"]
    if val in gate:
        break
    else:
        print('please input a or c')
if val == 'a':
    Question.askquestion(uid)
    Question.askweight(uid)
else:
    CompareResults.compare(uid)




