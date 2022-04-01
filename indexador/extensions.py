import psycopg2
import sqlite3
from  .settings import DATABASE_URL, ENVIROMENT

def getcon():

    if ((ENVIROMENT == 'production-heroku')  or (ENVIROMENT == 'development-bdremote') or (ENVIROMENT == 'development-fulllocal')) : 
        
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
          
    else:
        conn = sqlite3.connect(DATABASE_URL, check_same_thread=False)
        conn.row_factory = sqlite3.Row # its key esto es para que se pueda acceder al field por su nombre

    return conn

