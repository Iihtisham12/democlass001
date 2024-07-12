import usemore

while True:
    usemore.print_menu()
    user_input_choise = int(input("\nEnter Ur Choise : "))

    if user_input_choise == 1:
        usemore.check_employee()

    elif user_input_choise == 2:
        usemore.add_employee()

    elif user_input_choise == 3:
        usemore.delete_employee()

    elif user_input_choise == 4:
        usemore.get_all_employee()

    elif user_input_choise == 5:
        usemore.clear_screen()

    elif user_input_choise == 6:
        exit()

    else:
        print('Sorry You Enter Worng Data....')