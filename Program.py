from Bank import Account
from Bank import SavingsAccount
from Bank import ChecquingAccount
from Bank import Bank

def showMainMenu():
    print('What would you like to do?\n1. Open Account\n2. Select account\n3. Exit')

def showAccountMenu():
    print('What would you like to do?\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit Account to Main Menu')

def run():
    bank = 'RBC'

    while True:
        showMainMenu()
        option = (input('Enter choice (1-3): '))
        
        if option == 1:
            accountType = input('Enter account type (savings/checquing): ').lower()
            accountNumber = int(input ('Enter account number: '))
            accountHolder = str(input('Enter account holder name: '))
            rateOfInterest = float(input('Enter rate of interest: '))
            initialBalance = float(input('Enter initial balance to deposit'))

            if accountType == 'savings':

        elif option ==2:
            pass

        elif option == 3:
            pass

        else:
            pass
