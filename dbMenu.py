import readFilms, addFilms, updateFilms, deleteFilms, report

def read_file(file_path):
    try:
        with open(file_path) as open_file:
            rf = open_file.read()

            return rf
    
    except FileNotFoundError as not_found:
        print(f'File not found {not_found}')

# print(read_file('dbMenu.txt'))

def films_menu():
    option = 0
    optionsList = ['1','2','3','4','5','6']

    menu_choices = read_file('dbMenu.txt')

    while option not in optionsList:
        print(menu_choices)

        option = input('Enter an option from the menu choices above: ')

        if option not in optionsList:
            print(f'{option} is not a valid choice')
    
    return option

main_program = True

while main_program:

    menu_options = films_menu()

    if menu_options == '1':
        readFilms.read_allRecords()
    elif menu_options == '2':
        addFilms.insert_record()
    elif menu_options == '3':
        updateFilms.update_record()
    elif menu_options == '4':
        deleteFilms.delete_record()
    elif menu_options == '5':
        report.report()
    else:
        main_program = False
    
input('Press ENTER to exit: ')