# create a class Employee with attributes empid, name, salary 
# and also define methods to access properties of Employee.

class Employee:
    def __init__(self, empid=None, name=None, salary=None):
        self.empid = empid
        self.name = name
        self.salary = salary
    def setEmpid(self, empid):
        self.empid = empid
    def setName(self, name):
        self.name = name
    def setSalary(self, salary):
        self.salary =salary

    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name 
    def getSalary(self):
        return self.salary

e1 = Employee()
e2 = Employee(1, "Amit", 500000000)
e1.setEmpid(2)
e1.setName("Aman")
e1.setSalary(500000)

print(e1.getEmpid(), e1.getName(), e1.getSalary())
print(e2.getEmpid(), e2.getName(), e2.getSalary())