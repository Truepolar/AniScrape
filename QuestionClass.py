import numpy as np
import collections


u1 = []
w1 = []

#Question Class

class Question():
    def __init__(self, question, options, check, answer):
        self.question = question
        self.options = options
        self.check = check
        self.answer = answer

    def qchecker(self, ans):
        if ans not in self.check:
            return False
        return True

    def askquestion(self):
        print(self.question)
        print(self.options)


q1 = Question("1.Political alignment", " a.Left \n b.Right", {"a", "b"}, 0)
q2 = Question("2.Gender", " a.Male\n b.Female", {"a", "b"}, 0)
q3 = Question("3.Monthly income","a.0-3k \n b.3k-5k \n c.5k-8k \n d.8k-12k \n e.12k and above \n f.Does not matter",{"a","b","c","d","e","f"},0)
q4 = Question("4.Height in cm","a.140-150 \n b.150-160 \n c.160-170 \n d.170-180 \n e.180 and above \n f.Does not matter",{"a","b","c","d","e","f"},0)
q5 = Question("5.interests","a.Reading \n b.Music \n c.Making music \n d.Gaming \n e.Sports \n f.Food \n g.others",{"a","b","c","d","e","f","g"},0)

all_questions = [q1,q2,q3,q4,q5]

for q in [q1, q2,q3,q4,q5]:
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

# Weight for question class (new naming convention)

print('_' * 40)

print("Please rank the questions in order of least important to most important")

for q in all_questions:
    print(q.question)

wcheck = []
for i in range(1,len(all_questions) + 1):
    wcheck.append('i')

print(wcheck)

uw = []
gay = True

while gay == True:

    uw = input("Ranking from most to least (seperate ans with comma)").split(",")
   # uw.replace("'", "")
    if wcheck != sorted(uw):

        print(sorted(uw))
        gay = True




















# mylist = [ "a", "b", "a"]
#
# myset= set(mylist)
# myset.add("a")
# myset.add("az")
# myset.add("az")
#
# print(mylist)
#
# print(myset)
#
# for i in range(1,10, 3) :
#     print(i)




