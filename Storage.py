
import dotenv
import psycopg2
from dotenv import load_dotenv
from decouple import config

database = config('database')
host = config('host')
user = config('user')
password = config('password')
port = config('port', cast=int)

print(host)

conn = psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS questiondata (
userid INT PRIMARY KEY,
questionans STR,
questionweight INT,
ticket1 INT,
ticket2 INT);
""")

conn.commit()

cur.close()
conn.close()



class Inout:
    def __init__(self,level):
        self.level = level


