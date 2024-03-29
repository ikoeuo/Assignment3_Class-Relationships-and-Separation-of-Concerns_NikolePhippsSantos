class Account:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance, overdraftAllowed):
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.rateOfInterest = rateOfInterest
        self.currentBalance = currentBalance
        self.minimumBalance = minimumBalance
        self.overdraftAllowed = overdraftAllowed

    def getAccountNumber(self):
        return self.accountNumber
    
    def getAccountHolderName(self):
        return self.accountHolderName
    
    def getRateOfInterest(self):
        return self.rateOfInterest
    
    def getCurrentBalance(self):
        return self.currentBalance
    
    def deposit(self, amount):
        if amount > 0:
            self.currentBalance += amount
            print(f'Deposit successful, Your new balance is: {self.currentBalance}')
        else:
            print('Invalid deposit amount')

class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance, 0)

    def withdraw(self, amount):
        self.currentBalance -= amount
        if self.currentBalance < self.minimumBalance:
            print('Unable to withdraw amount')
            self.currentBalance += amount
        elif amount > 0 and self.currentBalance >= self.minimumBalance:
            print(f'Successfully withdrew {amount}, new balance is {self.currentBalance}')
        else:
            print('Error please try again.')

class ChequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftAllowed):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance, 0, overdraftAllowed)

    def withdraw(self, amount):
        self.currentBalance -= amount
        if self.currentBalance < self.overdraftAllowed:
            print('Unable to withdraw amount')
            self.currentBalance += amount
        elif amount > 0 and self.currentBalance >= self.overdraftAllowed:
            print(f'Successfully withdrew {amount}, new balance is {self.currentBalance}')
        else:
            print('Error please try again.')

class Bank(SavingsAccount, ChequingAccount, Account):
    def __init__(self, bankName):
        self.bankName = bankName 
        self.accounts = []

    def openChequingAccount(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftAllowed):
        account = ChequingAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftAllowed)
        self.accounts.append(account)
        print(f'Your new bank account {account.getAccountNumber()} has been opened!')
        return account

    def openSavingsAccount(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        account = SavingsAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance)
        self.accounts.append(account)
        print(f'Your new bank account {account.getAccountNumber()} has been opened!')
        return account

    def searchAccount(self, accountNumber):
        for account in self.accounts:
            if account.getAccountNumber() == accountNumber:
                return account
        print(f'Account does not exist.')

