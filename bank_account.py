class BankAccount: 

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    # def withdrawal(self, amount):
    #     if (self.balance - amount) <= 0:
    #         print("Insufficient funds: Charging a $5 fee")
    #         self.balance -= 5
    #     else:
    #         self.balance -= amount
    #         return self

    def withdrawal(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    # def yield_interest(self):
    #     if self.balance <= 0:
    #         print("Insuficiant Funds: No interest rate applied")
    #     else:
    #         self.balance += (self.balance * self.int_rate)
    #     return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("Insuficiant Funds: No interest rate applied")
        return self


    @classmethod
    def sum_all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

account1 = BankAccount(.03,600)
account2 = BankAccount(.01,200)

account1.deposit(1000).deposit(2000).deposit(5000).withdrawal(3000).yield_interest().display_account_info()
account2.deposit(80).deposit(200).withdrawal(100).withdrawal(300).withdrawal(50).withdrawal(100).yield_interest().display_account_info()

print(BankAccount.sum_all_balances())