while True:
    print('\n')
    print('_'*100)
    print('\n')
    print('\t \t -------------WELCOME TO THE MAIN PANEL OF MANAGEMENT-------------')
    print('''Choose user login type-
        1. Administrator Login.
        2. Customer Services''')

    Login_type = (input('Enter the way: ')).strip().lower()

    if  ((Login_type == 'administrator') or (int(Login_type) == 1)):
        original_password = 'Gurwinder'
        password = input('Enter the password to enter: ')
        if password == original_password:
            while True:
                print(' hello')
                break
        else: 
            print('Enter correct password')

    elif (Login_type == 'customer' or int(Login_type) == 2):
        password = input('Enter the password to enter: ')
        if password == original_password:
            while True:
                print(' hello')
                break
        else: 
            print('Enter correct password')

    else: 
        print('Invalid Choice.')

    print('*'*100)