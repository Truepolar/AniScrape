u1 = []
w1 = []

class Question():
    def __init__(self, question, options, check,):
        self.question = question
        self.options = options
        self.check = check

    def qchecker(self, ans):
        if ans not in self.check:
            return False
        return True

    def askquestion(self):
        print(self.question)
        print(self.options)


