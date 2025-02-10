import dotenv
from dotenv import load_dotenv
import psycopg2
from decouple import config

class UserData:
    def __init__(self,uid,name,password,age,gender):
        self.uid = uid
        self.name = name
        self.password = password
        self.age = age
        self.gender = gender

    def storeUD(self,uid,name,password,age,gender):
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

        cur.execute("INSERT INTO userdata (uid,name,password,age,gender) "
                    "VALUES (%s, %s, %s, %s)",
                    (uid,name,password,age,gender))




database = config('database')
host = config('host')
user = config('user')
password = config('password')
port = config('port', cast=int)

conn = psycopg2.connect(host=host,
database = database,
user = user,
password = password,
port = port
)

cur = conn.cursor()
cur.execute("SELECT uid FROM userdata")
print(cur.next())


