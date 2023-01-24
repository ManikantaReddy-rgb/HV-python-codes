# Create a class - Employee for two employees with some objects. 
# Fetch name,age and salary and display it in the screen.

#This is creating a class

class Employee:

    company="Aditya college"  #This is a class attribute

    def __init__(self,name,age,salary): #default constructor
        #name,age and salary are attributes
        self.name=name
        self.age=age
        self.salary=salary

#Creating objects
emp1=Employee("Revi",20,30000)
emp2=Employee("vicky",20,30000)

print(f"{emp1.name} and {emp2.name} works in {emp1.__class__.company}") #formatted string
print(f"{emp1.name} 's age is {emp1.age} and salary is {emp1.salary}")
print(f"{emp2.name} 's age is {emp2.age} and salary is {emp2.salary}")

