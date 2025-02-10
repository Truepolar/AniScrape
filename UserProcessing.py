import dotenv
from dotenv import load_dotenv
import psycopg2
from decouple import config

class UserData:
    def __init__(self,name = None,password = None,age = None,gender = None):
        self.name = name
        self.password = password
        self.age = age
        self.gender = gender


    def get_user(self):
        print('Hello new user.\nWhat is your name?')
        name = input('name: ')
        self.name = name
        print("Hello " + name)
        while True:
            confirm = 'no'
            print("Please enter a password")
            password = input("Password : ")
            print("Please enter password again")
            confirm = input("Password : ")
            if password == confirm:
                break
            else:
                print("Passwords do not match. \nPlease try again")
        self.password = password
        print("What is your age?")
        age = input('Age : ')
        self.age = age
        print("What is your gender, Male or Female?")
        while True:
            genderoptions = ["Male","male","Female","female"]
            gender = input("Gender : ")
            if gender not in genderoptions:
                return True
            else:
                break
        self.gender = gender



    def storeUD(self):
        database = config('database')
        host = config('host')
        user = config('user')
        password = config('password')
        port = config('port', cast=int)

        conn = psycopg2.connect(host=host,
                                database=database,
                                user=user,
                                password=password,
                                port=port
                                )
        cur = conn.cursor()

        cur.execute("INSERT INTO userdata (name,password,age,gender) "
                    "VALUES (%s, %s, %s, %s)",
                    (self.name,self.password,self.age,self.gender))

        conn.commit()
        cur.close()
        conn.close()







# cur = conn.cursor()
# cur.execute("SELECT  FROM userdata")
# #rint(cur.fetchall())
# for rec in cur :
#     print(f"Rec = {rec}")

