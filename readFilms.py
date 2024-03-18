from connect import *

def read_allRecords():
    try:
        dbCon, dbCursor = db_access()

        all_records = dbCursor.execute('SELECT * FROM tblFilms')

        all_records = dbCursor.fetchall()

        if all_records:
            print('*' * 160)
            print(f"filmID{'':<4}|title{'':<30}|yearReleased{'':<18}|rating{'':<24}|duration{'':<22}|genre{'':<10}")
            print('*' * 160)

            for aRecord in all_records:
                print(f'{aRecord[0]:<9} |{aRecord[1]:<35}|{aRecord[2]:<30}|{aRecord[3]:<30}|{aRecord[4]:<30}|{aRecord[5]:<10}')
                print('-' *160)

        else:
            print('No films found on this table')
    
    except sql.OperationalError as oe:
        print(f'Failed to read because: {oe}')


if __name__ == '__main__':
    read_allRecords()