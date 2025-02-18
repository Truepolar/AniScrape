# import dotenv
# from dotenv import load_dotenv
# import psycopg2
# from decouple import config
from user_store import *
from question import *
from user import *

u1 = []
w1 = []

user = User()

user.get_user()

UserStore.storeu(user)

Question.askquestion()


print("Please rank the questions in order of least important to most important")

for q in all_questions:
    print(q.question)

wcheck = []
for i in range(1, len(all_questions) + 1):
    wcheck.append(i)

print(wcheck)

uw = []
gay = True

while gay:
    uw = input("Ranking from most to least (separate ans with comma)").split(",")
    uw = list(map(int, uw))

    if wcheck == sorted(uw):
        gay = False

print(uw)

for i in wcheck:
    w1.append(uw.index(i) + 1)

print(w1)
