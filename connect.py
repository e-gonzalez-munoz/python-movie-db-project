import sqlite3 as sql

def db_access():
    try:
        with sql.connect('filmflix.db') as dbCon:
            dbCursor = dbCon.cursor()
            return dbCon, dbCursor
    except sql.OperationalError as oe:
        print(f'Connection failed: {oe}')