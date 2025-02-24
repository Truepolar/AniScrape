from user_store import *
from question import *
from register_user import *
from answer_store import *
RegisterUser.initial_page()

# -------------------------------

with get_session() as sess:
    name = input('please enter your name')
    stmt = select(UserData).where(UserData.name.in_([name]))
    for row in sess.scalars(stmt):
        print(row.uid)
        uid = row.uid

# -------------------------------

Question.askquestion(uid)


Question.askweight(uid)

