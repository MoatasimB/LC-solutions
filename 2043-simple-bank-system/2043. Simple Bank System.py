class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.withdraw(account1, money):
            if self.deposit(account2, money):
                return True
            else:
                self.deposit(account1, money)
        
        return False

        

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n:
            self.balance[account - 1] += money
            return True
        
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if 1<=account<=self.n and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)