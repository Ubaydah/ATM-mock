"""
A mock up ATM project that allows a user to
perform some operations in the atm
"""

from datetime import datetime
import random

#create a database for existing users 
database = {1234567890: ["Tundun", "Ubay", "ubay@gmail.com", "ubay20", 100],
            2987453090: ["Seyi", "Xyluz", "seyi@gmail.com", "seyi20", 300],
            2345127890: ["Mike", "Lore", "mike@gmail.com", "mike20", 400]
            }

#Initializes the app

def init():
    print(datetime.now())
    print("Welcome to Tyler's bank ATM")
    haveAccount = int(input("Do you have an account with us? (1) Yes (2) No \n"))
    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        print("You do not have account with us")
        Register = int(input("Will you like to open an account with us? (1) Yes (2) No \n"))
        if Register == 1:
            register()
        else:
            init()
    else:
        print("You have entered an invalid option")
        init()

#Generate account number 
 
def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def get_current_balance():
    for accountNumber, userDetails in database.items():
        return userDetails[4]


#The register function

def register():
    print("===================")
    print("Register")
    firstName = input("Enter your firstname \n")
    lastName = input("Enter your lastname \n")
    email = input("Enter your email \n")
    password = input("Create a password for yourself \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [firstName, lastName, email, password, 0]
    print("Your account has been successfully created")
    print("============================")
    print("This is your account number: %d " %accountNumber)
    print("= ==== ==== == ===== ===== =====")
    
    options = int(input("Will you like to login to your account? (1) Yes (2) No \n" ))
    if options == 1:
        login()
    else:
        init()
    
#The login function

def login():
    print("************Login************* ")
    accountNumberFromUser = int(input("Enter your account number \n"))
    passwordFromUser = input("Enter your password \n")
    accountNumbers = list(database.keys())
    userDetails = list(database.values())
    passwords = [i[3] for i in userDetails]
    if accountNumberFromUser in accountNumbers:
        if passwordFromUser in passwords:
            atmOperations()
    else:
        print("Invalid account or password")
        login()
    
    atmOperations()

#The atm-operations function

def atmOperations():
    print("You have successfully logged in Dear customer")
    print('These are the available options')
    print('1. Withdrawal')
    print('2. Cash deposit')
    print('3. Complaint')
    print('4. Logout')
    print('5. Exit')
    selectedOption = int(input('Please select an option \n'))
    
    if selectedOption == 1:
        Withdrawal()
    elif selectedOption == 2:
        cashDeposit()
    elif selectedOption == 3:
        complaint()
    elif selectedOption == 4:
        login()
    elif selectedOption == 5:
        exit()
    else:
        print('Invalid option selected, please try again')
        atmOperations()

#The withdrawal function that allows the user to withdraw

def Withdrawal():
    print("You have selected option 1")
    amount_to_withdraw = int(input("Enter amount you want to withdraw \n"))
    current_balance = get_current_balance()
    if current_balance > amount_to_withdraw:
        new_balance = current_balance - amount_to_withdraw
        print("Take your cash")
        print("New balance: ", new_balance) 
    else:
        print("You have insufficient balance")
        init()

#The deposit function that allows the user to deposit funds
def cashDeposit():
    current_balance = get_current_balance()
    amount_to_deposit = int(input("Enter amount to deposit "))
    new_balance = current_balance + amount_to_deposit
    print("Money recieved")
    print("Your new balance is:", new_balance)
    init()

#The complaint function that allows the user to make complaints
def complaint():
    complain = input("Enter your complain\n")
    print("Your complain is duly noted")
    init()
init()
