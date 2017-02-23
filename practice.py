class leCustomer:

    def __init__ (self, first, last, balance, password):
        self.first = first
        self.last = last
        self.balance = balance
        self.password = password

    def printName(self):
        return self.first + " "+ self.last

    def balance(self):
        return self.balance + ""

    def deposit(self):
        x = int(raw_input("How much do you want to deposit into your account?"))
        return self.balance + x

    def withdrawal(self):
        x = int(raw_input("How much do you want to withdraw from your account?"))
        return self.balance - x

    def changePassword(self):
        newPass = raw_input("Put in new password.")
        self.password = newPass

class Investor(Employee):
    def __init__ (self, first, last, balance, password, stock=None):
        super(Investor, self).__init__(first, last, balance, password)
        if stock == None:
            stock = {}
        else:
            stock = None





inv1 = Investor( first, last, balance, password, {"amazon": 50000, "apple": 30000})

c1 = leCustomer("Solomon", "Martinez", 1000000, "kittenmitten")
#print c1.printName()
#print c1.balance()
#print c1.deposit()
#print c1.withdrawal()
#print c1.changePassword()
#print c1.password
