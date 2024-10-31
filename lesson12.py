class Account:
    def __init__(self,full_name,acc_num,phone,balance): #method/function generator --> set up info
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount ${amount} deposited successfully to account {self.acc_num}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds.Balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"Amount ${amount} withdrawn successfully from account {self.acc_num}")

    def check_balance(self):
        print(f"Balance for account ${self.acc_num} is: {self.balance}")


kevo_acc = Account("Kevin Maina","0001","0712245678",1000)
sara_acc = Account("Sarah Hassan","0002","0712245678",1000)
kevo_acc.deposit(2000)
kevo_acc.check_balance()
kevo_acc.withdraw(1200)
kevo_acc.check_balance()


sara_acc.deposit(4000)
sara_acc.check_balance()
sara_acc.withdraw(1000)
sara_acc.check_balance()