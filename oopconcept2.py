# create a class called   Person with name,age and gender as attributes,constructor ,method and an object

class Person:
    def __init__(self,name,age,gender): #constructor
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):                  #method
        print("My name is {}, a  {} and am {} years old".format(self.name,self.gender,self.age))

myObj=Person("George",20,"male")        #creation of an object of class Person
myObj.display()                         #access the object's method using the dot operator(.)