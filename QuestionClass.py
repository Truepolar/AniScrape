import numpy as np

u1 = []


class Question():
    def __init__(self, question, options, check, answer):
        self.question = question
        self.options = options
        self.check = check
        self.answer = answer

    def checker(self, ans):
        if ans not in self.check:
            return False
        return True

    def askquestion(self):
        print(self.question)
        print(self.options)


q1 = Question("1.Political alignment", " a.Left \n b.Right", {"a", "b"}, 0)
q2 = Question("2.Gender", " a.Male\n b.Female", {"a", "b"}, 0)

for q in [q1, q2]:
    prompt = f"""
    {q.askquestion()}
    """
    while True:
        val = input()
        gate = q.checker(val)
        if gate:
            print("very interesting")
            break
        else:
            print("read the damn options retard")

    u1.append(val)

    print('_' * 40)

print(u1)
