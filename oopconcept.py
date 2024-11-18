class Fruits:
    def __init__(self,name,price,color): #constructor
        self.name=name
        self.price=price
        self.color=color
    def dispay(self): #class method
        print("My favorite fruit is {},its price is {} and it is {} in color".format(self.name,self.price,self.color))
myObj=Fruits("banana",10,"yellow") 
myObj.dispay()