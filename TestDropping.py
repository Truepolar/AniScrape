import dotenv
from dotenv import load_dotenv
import psycopg2
from decouple import config
from UserProcessing import *

#
# database = config('database')
# host = config('host')
# user = config('user')
# password = config('password')
# port = config('port', cast=int)
#
# conn = psycopg2.connect(host=host,
#                         database=database,
#                         user=user,
#                         password=password,
#                         port=port
#                         )
# cur = conn.cursor()
#
# cur.execute('DROP TABLE questiondata')
#
# conn.commit()
#
# cur.close()
# conn.close()


