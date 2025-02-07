
import dotenv
import psycopg2
from dotenv import load_dotenv
from decouple import config



database = config("database"),
host = config("host"),
user = config("user"),
password = config("password"),
port = config("port")

conn = psycopg2.connect(database=database,
                        host=host,
                        user=user,
                        password=password,
                        port=port)
