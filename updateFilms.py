from connect import *

def update_record():
    try:
        dbCon, dbCursor = db_access()

        film_id = int(input('Enter the FilmID to update a record'))
        dbCursor.execute('SELECT * from tblFilms where filmID = ?', (film_id,))

        row = dbCursor.fetchone()

        if row == None:
            print(f'No record with FilmID {film_id} has been found')

        else: 
            num_fields = input('Enter N to update one field or Y to update all fields: ').upper()

            if num_fields == 'Y':
                 film_title = input('Enter value to update the film title: ')
                 release_year = input('Enter value to update the release year: ')
                 film_rating = input('Enter value to update the film rating: ')
                 film_duration = input('Enter value to update the film duration (in minutes): ')
                 film_genre = input('Enter value to update the film genre: ')
                 
                 dbCursor.execute('UPDATE tblFilms (SET title =?, SET yearReleased =?, SET rating =?, SET duration =?, SET genre = ?)', (film_title, release_year, film_rating, film_duration, film_genre))
                 dbCon.commit()
                 print(f'All fields in the record {film_id} have been updated on the Films table')
                 
            elif num_fields == 'N':
                field_name = input('Enter the field (title or yearReleased or rating or duration or genre): ')
                if field_name not in ['title', 'yearReleased', 'rating', 'duration', 'genre']:
                    print(f'Field {field_name} not a valid field name in the table')
                else:
                    field_value = input(f'Enter the value for the field {field_name}: ')

                    dbCursor.execute(f"UPDATE tblFilms SET {field_name} =? WHERE filmID =?", (field_value, film_id,))
                    dbCon.commit()
                    print(f"Record {film_id} updated in the films table")
            else:
                print('Invalid choice, please enter Y or N')
        
    except sql.OperationalError as oe:
        print(f'Update failed: {oe}')

if __name__ == '__main__':
    update_record()
            
