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
        
        if option == 1: #Open Account

            accountType = input('Enter account type (savings/checquing): ').lower()
            accountNumber = int(input ('Enter account number: '))
            accountHolder = str(input('Enter account holder name: '))
            rateOfInterest = float(input('Enter rate of interest: '))
            initialBalance = float(input('Enter initial balance to deposit'))

            if accountType == 'savings':
                account = SavingsAccount(accountNumber, accountHolder, rateOfInterest, initialBalance , SavingsAccount.minimumBalance)
                #Account Number: {accountNumber}, Account Holder: {accountHolder}, Rate Of Interest: {rateOfInterest}, Current Balance: {Bank.currentBalance}, Minimum Balance:{minimumBalance}

            elif accountType == 'checquing':
                account = ChecquingAccount(accountNumber, accountHolder, rateOfInterest, initialBalance , ChecquingAccount.overdraftAllowed)

            else:
                print('Unable to open account, Invalid account type.')

            Bank.openAccount(account)

        elif option == 2: #2. Select account

            accountNumber = input('Enter Account Number: ')
            Bank.searchAccount
            if accountNumber is account:
                while True:
                    showAccountMenu()
                    accountOption = print(input('Enter selection (1-4): '))

                    if accountOption == 1: #Check Balance
                        print('Your current balance is: ')
                        Account.getCurrentBalance() 

                    elif accountOption == 2: #2. Deposit
                        amount = print(float(input('How much money would you like to deposit? ')))
                        Account.deposit(amount)

                    elif accountOption == 3: #3. Withdraw
                        amount = print(float(input('How much money would you like to withdraw? ')))
                        Account.withdraw(amount)

                    elif accountOption == 4: #4. Exit Account to Main Menu
                        break

        elif option == 3: #3. Exit
            print('Thank you for using my app!')

        else:
            print('Invalid Selection')
