import numpy as np
import collections
from ResultsProcessing import *
from initstorage import *

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


