# 1.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(f"The name of the person is {self.name} and age is {self.age}")

# p1 = Person("Amit", 20)
# p1.show()

# 2.
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     # getter
#     def get_radius(self):
#         return self.radius
    
#     # setter
#     def set_radius(self, radius):
#         self.radius = radius
        
#     # methods
#     def getArea(self):
#         return 3.14 * self.radius * self.radius
#     def getCircumference(self):
#         return 2 * 3.14 * self.radius
# c1 = Circle(3)
# print("Area:", c1.getArea())
# print("Circumference:", c1.getCircumference())

# 3.
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
    

#     def setDimensions(self,length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def showDimensions(self):
#         return f"The length of given rectangle is {self.length} and breadth is {self.breadth}"

#     def getArea(self):
#         return self.length * self.breadth
    
# r1 = Rectangle(4, 5)
# print("Dimnsions:", r1.showDimensions())
# print("Area of given rectangle is:", r1.getArea())

# 4.
# class Book:
#     def __init__(self, bookid, title, price):
#         self.bookid = bookid
#         self.title = title
#         self.price = price
#     def ShowBook(self):
#         return f"Book ID: {self.bookid}, Book Title: {self.title}, Book Price: {self.price}"

# b1 = Book(10001, "DSA using Python", 1000)
# print("Details:", b1.ShowBook())

# 5.
class Team:
    def __init__(self, memberNames):
        self.memberNames = memberNames

    def addMemberName(self, memberName):
        self.memberNames.append(memberName)
    
    def displayNames(self):
        print(f"Team members are: {self.memberNames}")
    
t1 = Team(["Amit"])
t1.addMemberName("Mann")
t1.addMemberName("Vidya")
t1.addMemberName("Mono")


print(t1.displayNames())