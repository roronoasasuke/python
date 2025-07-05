class account:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'deposited {amount} coins ,mr krabs is pleased')
        else:
            print('you cant deposit zero gold')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'withdraw {amount} coins , watever')
        else:
            print('Insufficient balance ahhahahah noob')

    def get_balance(self):
        return self.__balance

acc = account(100000000000)
acc.deposit(500)        
acc.withdraw(1000)                        
print('Current balance:',acc.get_balance())