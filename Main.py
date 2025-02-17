# import dotenv
# from dotenv import load_dotenv
# import psycopg2
# from decouple import config
from userstore import *
from questionask import *
from userask import *

u1 = []
w1 = []

q1 = Question("1.Political alignment", "a.Left \n b.Right", {"a", "b"})
q2 = Question("2.Gender", " a.Male\n b.Female", {"a", "b"})
q3 = Question("3.Monthly income", "a.0-3k \n b.3k-5k \n c.5k-8k \n d.8k-12k \n e.12k and above \n f.Does not matter",
              {"a", "b", "c", "d", "e", "f"})
q4 = Question("4.Height in cm",
              "a.140-150 \n b.150-160 \n c.160-170 \n d.170-180 \n e.180 and above \n f.Does not matter",
              {"a", "b", "c", "d", "e", "f"})
q5 = Question("5.interests", "a.Reading \n b.Music \n c.Making music \n d.Gaming \n e.Sports \n f.Food \n g.others",
              {"a", "b", "c", "d", "e", "f", "g"})

all_questions = [q1, q2, q3, q4, q5]

user = UserData()

user.get_user()

Ustore.storeu(user)

for q in [q1, q2, q3, q4, q5]:
    prompt = f"""
    {q.askquestion()}
    """
    while True:
        val = input()
        gate = q.qchecker(val)
        if gate:
            print("very interesting")
            break
        else:
            print("read the damn options retard")

    u1.append(val)

    print('_' * 40)

print(u1)

print('_' * 40)

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
