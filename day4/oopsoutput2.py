class Mobile:
     def _init_(self,brand,price):
         self.brand = brand
         self.price = price
         self.total_price = None
     def purchase(self):
         if self.brand == "apple":
             discount = 10
         else:
             discount = 5
         self.total_price = self.price - self.price *(discount/100)
         print("Total price of",self.brand,"mobile is",self.total_price)
     def amount_returned(self):
         return (self.price-self.total_price)

mob1=Mobile("apple",20000)
mob2=Mobile("samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())

class Customer:
    def _init_(self,cust_id,name,age,wallet_balance):
         self.cust_id = cust_id
         self.name = age
         self.wallet_balance = wallet_balance
    def update_balance(self,amount):
         if amount < 1000 and amount > 0:
             self.wallet_balance += amount
    def show_balance(self):
         print("the balance is ",self.wallet_balance)

c1=Customer(100,"Gopal",24,1000)
c1.update_balance(500)
c1.show_balance()

  
