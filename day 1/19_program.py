"""  Find the number of distinct subarrays in an array of position integers such that the sum of the subarray is an odd integer,
two subarray are considered different if they start or end at different index input.

1
3
1 2 3
[1] [1 2] [1,2,3] [2] [2,3] [3]
4                                                        """



n1=int(input("Enter a value"))
n2=int(input("Enter a value"))
array=[i for i in range(n1,n2+1)]
print(array)
result=[]
for i in range (len(array)) :
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
#result=[array[i:j+1] for i in range(len(array)) for j in range (i,len(array))]#single line code
#print(result)
c=0
for i in result:
    if sum(i) % 2 !=0:
        c+=1
print (c)