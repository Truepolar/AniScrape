import dotenv
from dotenv import load_dotenv
import psycopg2
from decouple import config

class Processing:

    def __init__(self,w1,u1):
        self.inweight = inw
        self.w1 = w1
        self.u1 = u1
        self.ticket1 = ticket1
        self.ticket2 = ticket2
        self.userid = userid

    def storagein(self,userid,w1,u1):
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
        cur.execute("")

    def newid(self):
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
        conn = psycopg2.connect(host=host,
                                database=database,
                                user=user,
                                password=password,
                                port=port
                                )

