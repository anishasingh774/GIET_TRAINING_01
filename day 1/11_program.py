#list-->Ordered--default index
#
list1=[]
print(list1,type(list1))
list2=[10,20,30,40]
print (list2,type(list2))
list3=[10,20.2,30.3j,True,"python"]
print (list3,type(list3))
list4=list([100,200,300,400])
print (list4,type(list4))
list5=[101,201,301,401]
print (list5,type(list5))
list5.append(501)
print (list5,type(list5))
list5.extend((100,200,300))
print (list5,type(list5))
list5.insert(0,51)#index,value
print (list5,type(list5))
list5.remove(201)
print (list5,type(list5))
list5.pop()
print (list5,type(list5))
list5.pop(0)
print (list5,type(list5))
del list5[1]
print (list5,type(list5))

