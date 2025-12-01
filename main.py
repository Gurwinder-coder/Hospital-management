while True:
    print('\n')
    print('_'*100)
    print('\n')
    print('\t \t -------------WELCOME TO THE MAIN PANEL OF MANAGEMENT-------------')
    print('''Choose user login type-
        1. Administrator Login.
        2. Patient Panel ''')

    Login_type = (input('Enter the way: ')).strip().lower()

    if  ((Login_type == 'administrator') or (int(Login_type) == 1)):
        print('''\t1.Medicine Stock
        2.Total revenue
        3.Total revenue visulisation
        4.Medical Certificates issued ''')
        
        service = input('Choose the service you want: ').strip().lower()
        match service:
            case '1' | 'medical stock': pass
            case '2' | 'total revenue': pass
            case '3' | 'total revenue visulisation': pass
            case '4' | 'medical certificates issued': pass


    elif (Login_type == 'patient' or int(Login_type) == 2):
        print('''\t1.Patient List 
        2.Add Patient
        3.Remove Patient 
        4.Patient Bills 
        5.Patient Report
        6.Visitor list''')
        
        service = input('Choose the service you want: ')
        match service:
            case '1' | 'patient list': pass
            case '2' | 'add patient': pass
            case '3' | 'remove patient': pass
            case '4' | 'patient bills': pass
            case '5' | 'patient report': pass
            case '6' | 'visitor list': pass

    else: 
        print('Invalid Choice.')

    print('*'*100)