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
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self.currentBalance = currentBalance
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
            super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
            self.currentBalance = currentBalance
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
    def __init__(self, bankName, account):
        self.bankName = bankName 
        self.accounts = []
        self.account = account

    def openChequingAccount(self, bankName, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftAllowed):
        super().__init__(bankName, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftAllowed)
        self.accounts.append(self.account)
        print(f'Your new bank account {Account.getAccountNumber()} has been opened!')

    def openSavingsAccount(self, bankName, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__(bankName, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance)
        self.accounts.append(self.account)
        print(f'Your new bank account {Account.getAccountNumber()} has been opened!')

    def searchAccount(self, accountNumber):
        for account in self.accounts:
            if Account.getAccountNumber == accountNumber:
                return account
            else:
                print(f'Account does not exist.')
