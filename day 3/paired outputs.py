# paired outputs
"""problem statement: For each number in list_b, get the number and its position(index) in mylist as a return list of tuples
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[(6,2),(4,8)]  """
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
res=[]
for j in list_b:
     for i in mylist:
         if(j==i):
             res.append((j,mylist.index(i)))
print(res)
m=dict(res)
print(m)
# OR
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
res={}
for i in list_b:
     res.append((i,mylist.index(i)))
print(res)
 #  dictionary comprehension
print([(i,mylist.index(i))for i in list_b])
res={}
for i in list_b:
    res[i]=mylist.index(i)
print(res)
print({i:mylist.index(i) for i in list_b})
  

