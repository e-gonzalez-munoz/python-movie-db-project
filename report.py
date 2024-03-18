from connect import *

def report():
    try:
        dbCon, dbCursor = db_access()

        search_field = input('Search by filmID or title or yearReleased or rating or duration or genre: ')

        if search_field == 'filmID':
            film_id = int(input('Enter Film ID: '))
            dbCursor.execute(f'SELECT * FROM tblFilms WHERE filmID = ?', (film_id,))

            row = dbCursor.fetchone()

            if row is None:
                print(f'No records with Film ID {film_id} have been found')
            else:
                print(row)

        elif search_field in ['title', 'yearReleased', 'rating', 'duration', 'genre']:

            str_input = input(f'Enter the value for the field {search_field}')

            dbCursor.execute(f'SELECT * FROM tblFilms WHERE {search_field} LIKE ?', (f'%{str_input}%',))

            rows = dbCursor.fetchall()

            if not rows:
                print(f'No records with the field {search_field} matching {str_input} have been found')
            else:
                for records in rows:
                    print(records)
        else:
            print(f'Search field {search_field} invalid')

    except sql.OperationalError as oe:
        print(f'Search error: {oe}')

if __name__ == '__main__':
    report()