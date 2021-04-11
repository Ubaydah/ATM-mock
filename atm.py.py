#register
#login to the atm
#atmoperations
from datetime import datetime
import random

#create a database for existing users 
database = {1234567890: ["Tundun", "Ubay", "ubay@gmail.com", "ubay20"],
            2987453090: ["Seyi", "Xyluz", "seyi@gmail.com", "seyi20"],
            2345127890: ["Mike", "Lore", "mike@gmail.com", "mike20"]
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
#   
def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def passwordCreate():
    passw = input("Create a password \n")
    if len(passw) > 10 :
        print("Your password is longer than 10 digits ")
        passwordCreate()

#The register function

def register():
    print("===================")
    print("Register")
    firstName = input("Enter your firstname \n")
    lastName = input("Enter your lastname \n")
    email = input("Enter your email \n")
    password = passwordCreate()

    accountNumber = generateAccountNumber()

    database[accountNumber] = [firstName, lastName, email, password]
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

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == passwordFromUser:
                atmOperations(userDetails)
        else:
            print("Invalid account or password")
            login()
    atmOperations(userDetails)

#The atm-operations function

def atmOperations(user):
    print("You have successfully logged in")
    print("Welcome %s %s " % ( user[0], user[1] ) )
    print('These are the available options')
    print('1. Withdrawal')
    print('2. Cash deposit')
    print('3. Complaint')
    selectedOption = int(input('Please select an option \n'))
    if selectedOption == 1:
        print('You selected', selectedOption)
        print('How much will you like to withdraw?')
        cash = int(input('Enter amount\n'))
        print('Take your cash')
        print("Thanks for banking with us")
    elif selectedOption == 2:
        print('You selected', selectedOption)
        print('How much would you like to deposit?')
        amount = float(input('Enter amount\n'))
        print('Your current balance is', amount)
        print("Thanks for banking with us")
    elif selectedOption == 3:
        print('You selected', selectedOption)
        print('What issue will you like to report')
        complaint = input('Enter your complaint\n')
        print('Thank you for contacting us')
    else:
        print('Invalid option selected, please try again')
        atmOperations(userDetails)

init()
