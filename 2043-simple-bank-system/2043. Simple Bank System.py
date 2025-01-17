class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.check(account1) or not self.check(account2) or money > self.balance[account1-1]:
            return False
        
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.check(account):
            return False
        
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.check(account) or money > self.balance[account-1]:
            return False
        
        self.balance[account -1] -= money
        return True

    def check(self, account):
        return 0<account<=len(self.balance)
# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)