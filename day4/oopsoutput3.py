class Table:
     def _init_(self):
         self.no_of_legs=4
         self.__glass_top=None
         self.__wooden_top=None
     def assign_data(self,glass_top,wooden_top):
         self.__glass_top=glass_top
         self.__wooden_top=wooden_top
     def identify_rate(self,glass_top,wooden_top):
         self.assign_data(glass_top,wooden_top)
         if(self.__glass_top==True):
             rate=20000
         elif(self.__wooden_top==True):
             rate=30000
         else:
             rate=0
         return rate
dinning_table=Table()
rate=dinning_table.identify_rate(False,True)
print(rate)


class Table:
    def _init_(self):
         self.no_of_legs=4
         self.glass_top=None
         self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)
  
