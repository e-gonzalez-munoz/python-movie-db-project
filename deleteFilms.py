from connect import *

def delete_record():

    try:
        dbCon, dbCursor = db_access()

        film_id = int(input('Enter the FILM ID to delete a record'))
        dbCursor.execute('SELECT * FROM tblFilms WHERE filmID = ?', (film_id,))

        row = dbCursor.fetchone()

        if row == None:
            print(f'No record with {film_id} exists')
        else:
            dbCursor.execute('DELETE FROM tblFilms WHERE filmID =?', (film_id,))
            dbCon.commit()

            print(f'The record with the FILM ID {film_id} has been deleted')

    except sql.OperationalError as oe:
        print(f'Failed to delete. Error: {oe}')
    
if __name__ == '__main__':
    delete_record()
