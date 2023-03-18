# for loop version--> odd elements
result=[]
for i in range(11):
     if i%2!=0:
        result.append(i)
     else:
         result.append(i**2)
print(result)
#OR
print([i if i%2!=0 else i**2 for i in range(11)])  
