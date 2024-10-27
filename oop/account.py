class Account:

    def __init__(self, acc_no, balance):
        # Private Variables (Conceptually hiding data)
        self.__acc_no = acc_no
        self.__balance = balance

    def debit(self, balance):
        self.__balance -= balance

    def credit(self, balance):
        self.__balance += balance
    
    def check(self):
        print("Hi! Balance for account number",self.__acc_no, "is $" + str(self.__balance))


acc = Account("091231", 200)
acc.debit(30)
acc.credit(70)
acc.check()