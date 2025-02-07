import dotenv
from dotenv import load_dotenv
class Processing:
    def __init__(self,inw):
        self.inweight = inw

    def inpro(self,inweight):
          ticket1 = inweight.index(1)
          ticket2 = inweight.index(2)

          print(ticket1,ticket2)

