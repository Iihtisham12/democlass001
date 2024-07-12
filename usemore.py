
import employee
import os

# Check Employee
def check_employee():
    id = int(input("Enter Employee ID : "))
    emp = employee.get_employee(id)
    if emp == 0:
        print("Employee Not Found. ")
    else:
        print("\n*** -----------Find Employee----------- ***")
        print("\nEmployee Found With Name  :  ", emp)

# Add Employee 
def add_employee():
    name = input("Enter Your Name : ")
    id = employee.add_employee(name)
    print('New User added with ID\t:  ', id)

# Delete Employee
def delete_employee():
    id = int(input("Enter Employee ID To Delete.. : "))
    if employee.delete_employee(id) != 0:
        print("User Deleted With ID ",id)
    else:
        print("Sorry No ID Matched to Delete !! ")

# All Employee Display In a List
def get_all_employee():
    employees = employee.get_employee()
    print("***","-"*15,"*","All Employees List","*","-"*15,"***\n",)
    for id, name in employees.items():
        print(f"ID of Employee \t : {id} \t Or \t Name of Employee  \t : {name}")

# Menu 
def print_menu(): 
    print("\n",'***','-'*20,'*','Options','*','-'*20,'***')
    print('1: Check Employee : ')
    print('2: Add Employee : ')
    print('3: Delete Employee : ')
    print('4: Display all Employee : ')
    print('5: Clear The Screen : ')
    print('6: Exit : ')

# Clear Screen 
def clear_screen():
    os.system("cls")