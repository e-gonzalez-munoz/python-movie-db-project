from connect import *

def insert_record():
    try:
        dbCon, dbCursor = db_access()

        film_title = input('Enter the film title: ')
        release_year = input('Enter the release year: ')
        film_rating = input('Enter the film rating: ')
        film_duration = input('Enter the film duration (in minutes): ')
        film_genre = input('Enter the film genre: ')


        dbCursor.execute('INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)', (film_title, release_year, film_rating, film_duration, film_genre))

        dbCon.commit()


        print(f'{film_title} has been inserted on the Films table')

    except sql.OperationalError as oe:
        print(f'Error, {oe}')

if __name__ == '__main__':
    insert_record()