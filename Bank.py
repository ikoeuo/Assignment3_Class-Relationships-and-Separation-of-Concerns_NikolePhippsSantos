class Account:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.rateOfInterest = rateOfInterest
        self.currentBalance = currentBalance

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
            print(f'Deposit  successful, Your new balance is: {self.currentBalance}')
        else:
            print('Invalid deposit amount')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.currentBalance:
            self.currentBalance -= amount
            print(f'Widthdrawl successful, Your new balance is: {self.currentBalance}.')
        else:
            print('Invalid deposit amount')

class SavingsAccount:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        self.currentBalance = 0
        self.minimumBalance = minimumBalance 
    def withdraw(self, amount):
        self.currentBalance = amount
        self.currentBalance -= amount

        if self.currentBalance < self.minimumBalance:
            print('Unable to widthdraw amount')
            self.currentBalance += amount

        elif amount > 0 and self.currentBalance >= self.minimumBalance:
            print(f'Sucessfully widthdrew {amount}, new balance is {self.currentBalance}')

        else:
            print('Error please try again.')

class ChecquingAccount:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftAllowed):
            self.currentBalance = 0
            self.overdraftAllowed = overdraftAllowed
    def withdraw(self, amount):
        self.currentBalance = amount
        self.currentBalance -= amount

        if self.currentBalance < self.overdraftAllowed:
            print('Unable to widthdraw amount')
            self.currentBalance += amount

        elif amount > 0 and self.currentBalance >= self.overdraftAllowed:
            print(f'Sucessfully widthdrew {amount}, new balance is {self.currentBalance}')

        else:
            print('Error please try again.')


class Bank:
    def __init__(self, bankName):
        self.bankName = bankName 
        self.accounts = []

    def openAccount(self, account):
        self.accounts.append(account)
        print(f'Your new bank account {Account.getAccountNumber()} has been opened!')

    def searchAccount(self, accountNumber):
        for account in self.accounts:
            if Account.getAccountNumber == accountNumber:
                return account
