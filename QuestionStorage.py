import dotenv
from dotenv import load_dotenv
import psycopg2
from decouple import config
from question import *

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

q1 = Question("1.Political alignment", " a.Left \n b.Right", {"a", "b"}, 0)
q2 = Question("2.Gender", " a.Male\n b.Female", {"a", "b"}, 0)
q3 = Question("3.Monthly income","a.0-3k \n b.3k-5k \n c.5k-8k \n d.8k-12k \n e.12k and above \n f.Does not matter",{"a","b","c","d","e","f"},0)
q4 = Question("4.Height in cm","a.140-150 \n b.150-160 \n c.160-170 \n d.170-180 \n e.180 and above \n f.Does not matter",{"a","b","c","d","e","f"},0)
q5 = Question("5.interests","a.Reading \n b.Music \n c.Making music \n d.Gaming \n e.Sports \n f.Food \n g.others",{"a","b","c","d","e","f","g"},0)
