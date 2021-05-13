# author : @akash kumar 

# parent class------------------------------------------------------------
class Vehicle:
    #Color,Price,Maximum_Speed ---->instance variable for parent class
    def __init__(self,Color,Price,Maximum_Speed): 
    #constuctor of parent class
        self.Color=Color
        self.Price=Price
        self.Maximum_Speed=Maximum_Speed
    def show(self):
        print("A "+self.Color+"-colored car with a mximum speed of "+str(self.Maximum_Speed)+" km/h is priced at "+str(self.Price)+" with ",end="")

#child class------------------------------------------------------------
class Car(Vehicle):
    def __init__(self,Color,Price,Maximum_Speed,Number_Of_Tires):
    #constructor for child class
        self.Number_Of_Tires=Number_Of_Tires

        Vehicle.__init__(self,Color,Price,Maximum_Speed)
        #inheritance process----

    def showtires(self):
        print(str(self.Number_Of_Tires)+" tires")

# variable or an instance----------------------------------------------
ans=Car("red",500000,200,4)
ans.show()
ans.showtires()
#---------------------------------------------------------------------
