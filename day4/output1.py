class Book:
     def _init_(self,):
         self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the hard way"
my_fav.title="Learning Python"
print("My favourite is",my_fav.title)
print("Your's is :",your_fav.title)
#
#  ------------------------------------------------------------------------------------
class shoe:
 def _init_(self,price,material):
     self.price=price
     self.material=material
s1=shoe(1000,"Canvas")
print(s1)
print(s1.price,s1.material)
