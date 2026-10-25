class InsufficientFundsError(Exception):
    pass
class BankAcount:
    acc_counter = 100

    def __init__(self, name, balance):
        self.name = name
        BankAcount.acc_counter += 1
        self.__acc = BankAcount.acc_counter
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount > self.__balance:
            self.__balance -= amount
        else:
            raise InsufficientFundsError()
    def get_balance(self):
        return self.__balance
    def get_detail(self):
        return f'Balance: {self.__balance}, {self.name}, {self.__balance }'
jame = BankAcount('jame', 100)
ashok = BankAcount('ashok', 200)
print(jame.get_detail())
print(ashok.get_detail())