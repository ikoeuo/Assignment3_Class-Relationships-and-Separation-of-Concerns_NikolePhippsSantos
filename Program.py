from Bank import Account, SavingsAccount, ChequingAccount, Bank

def showMainMenu():
    print('\nWhat would you like to do?\n1. Open Account\n2. Select account\n3. Exit')

def showAccountMenu():
    print('\nWhat would you like to do?\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit Account to Main Menu')

def run():
    bankName = 'RBC'
    bank = Bank(bankName)

    #adds pre made accounts, 2 of each :)
    account1 = SavingsAccount(1010, 'Jake Perez', 0.2, 22500, 1000)
    bank.accounts.append(account1)
    account2 = SavingsAccount(2020, 'Verinica Smith', 0.1, 6500, 1000)
    bank.accounts.append(account1)
    count3 = ChequingAccount(3030, 'Jake Park', 0.05, 550, -100)
    bank.accounts.append(account1)
    account4 = ChequingAccount(4040, 'Finn Santos', 0.25, 1330, -100)
    bank.accounts.append(account1)


    while True:
        showMainMenu()
        option = int(input('Enter choice (1-3): '))

        if option == 1: #Open Account
            accountType = input('Enter account type (savings/chequing): ').lower()
            accountNumber = int(input('Enter account number: '))
            accountHolder = str(input('Enter account holder name: '))
            rateOfInterest = float(input('Enter rate of interest: %'))

            if accountType == 'savings':
                initialBalance = 1000
                minimumBalance = 1000
                account = bank.openSavingsAccount(accountNumber, accountHolder, rateOfInterest, initialBalance, minimumBalance)
            elif accountType == 'chequing':
                initialBalance = 0
                overdraftAllowed = -100
                account = bank.openChequingAccount(accountNumber, accountHolder, rateOfInterest, initialBalance, overdraftAllowed)
            else:
                print('Unable to open account, Invalid account type.')

        elif option == 2: #2. Select account
            accountNumber = int(input('Enter Account Number: '))
            account = bank.searchAccount(accountNumber)
            if account:
                while True:
                    showAccountMenu()
                    accountOption = int(input('Enter selection (1-4): '))

                    if accountOption == 1: #Check Balance
                        print('Your current balance is:', account.getCurrentBalance())

                    elif accountOption == 2: #2. Deposit
                        amount = float(input('How much money would you like to deposit? '))
                        account.deposit(amount)

                    elif accountOption == 3: #3. Withdraw
                        amount = float(input('How much money would you like to withdraw? '))
                        account.withdraw(amount)

                    elif accountOption == 4: #4. Exit Account to Main Menu
                        break

                    else:
                        print('Invalid option')

            else:
                print('Bank account does not exist.')

        elif option == 3: #3. Exit
            print('Thank you for using my app!')
            exit()

        else:
            print('Invalid Selection')


run()
