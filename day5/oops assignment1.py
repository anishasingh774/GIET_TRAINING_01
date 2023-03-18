'''
WeCare insurance company wants to calculate premium of vehicles.
-->vehicles are of two types - "Two Wheeler" and "Four Wheelers"
each vehicle is identified by vehicle id, type, cost and premium amount.
--> Premium amount is 2% of the vehicle cost for two wheelers and
6% of the vehicle cost for four wheelers.
calculate the premium amount and display the vehicle details.
write a python program to implement the class chosen with its attributes and methods.
Note:
consider all instance variables to be private and methods to be public
include getter and setter methods for all instance variables , display appropriate error message,
error message, if the vehicle type is invalid
perform case snsitive string comparison
represent few objects of the class, initialize instance variables using setter methods,
 invoke appropriate methods and test your program.
 '''
#ans

class Vehicle:
    def _init_(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
        print(self.__vehicle_id)
    
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
        print(self.__vehicle_type)
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
        print(self.__vehicle_cost)
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
        print(self.__premium_amount)
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
         return self.__vehicle_cost
    def get_premium_amount(self):
        return self.__premium_amount
    def calculate_premium(self):
        if self.__vehicle_type=="Two Wheeler":
            self.__premium_amount=self.__vehicle_cost*0.02
        elif self.__vehicle_type=="Four Wheeler":
            self.__premium_amount=self.__vehicle_cost*0.06
    def display_vehicle_details(self):
        self.calculate_premium()
        print("the vehicle id is : ",self.__vehicle_id)
        print("The vehilcle type :" ,self.__vehicle_type)
        print("The vehicle cost is:",self.__vehicle_cost)
        print("The vehicle premium is:",self.__premium_amount)
s1=Vehicle()
s1.set_vehicle_id(121)
s1.set_vehicle_type("Two Wheeler")
s1.set_vehicle_cost(60000)
s1.calculate_premium()
s1.display_vehicle_details()


        

    


















        
