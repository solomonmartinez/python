class Employee(object):

    raiseAmount = 1.04
    numEmployee = 201
    hoursWorked = 40

    def __init__(self, first, last, pay): #Constructer
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com" #Constructer
    def printName(self):
        return self.first + " " + self.last

    def weeklyPay(self):
        return(self.hoursWorked * self.pay)

    #def raisePay(self, self.hours):
         #return employee_1.weeklyPay * raiseAmount

    def weeklyPayraise (self):
        return (self.hoursWorked * self.pay * self.raiseAmount)

    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount

    @classmethod
    def fromString(cls, empStr):
        first, last, pay = empStr.split('-')
        return cls(first, last, float(pay))

class Developer(Employee):
    def __init__(self, first, last, pay, Proglanguage):
        super(Developer, self).__init__(first, last, pay)
        self.Proglanguage = Proglanguage

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def removeEmp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmp(self):
        for emp in self.employees:
            print "---->" + emp.printName()

dev1 = Developer("Frank", 'Chipmunk', 12, "Python")
dev2 = Developer("Kit", "KAt", 90, "Swift")
man1 = Manager("Tom", "Lee", 15, [dev1])

print man1.employees[0].first
man1.addEmp(dev2)

#man1.printEmp()
