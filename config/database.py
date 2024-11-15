import cx_Oracle
import os
from dotenv import load_dotenv


def get_db_connection():
    try:
        dsn = cx_Oracle.makedsn(os.getenv("DB_HOST"), os.getenv("DB_PORT"), sid=os.getenv("DB_SID"))
        connection = cx_Oracle.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=dsn
        )
        return connection
    except cx_Oracle.DatabaseError as e:
        print("Error while connecting to Oracle Database", e)
        return None