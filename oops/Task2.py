# Create a class - Student. Use the method concept, 
# to fetch student name and marks for them


class Student:
    def __init__(self,name,marks): #default constructor
        #name,age and salary are attributes
        self.name=name
        self.marks=marks
        
    def getDetails(self):
        print(f"Hi! My name is{self.name},I received{self.marks}marks")

    def getDetails1(self):
        print(f"Hi! My name is{self.name},I received{self.marks}marks")

stud1=Student("ManikantaReddy",99)
stud2=Student("Mani",88)

stud1.getDetails()
stud2.getDetails1()
