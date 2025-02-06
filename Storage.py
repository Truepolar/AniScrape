import sqlite3

conn = sqlite3('Userdb')
c = conn.cursor()
c.execute("""CREATE TABLE user(




)""")
class Store:

   def __init__(self,user,passw,qans,qweight):
    self.username = user
    self.password = passw
    self.questionans = qans
    self.questionweight = qweight

   def keep(self,user,password,questionans,questionweight):

       Level1S = questionweight.index(1)

       c.execute


