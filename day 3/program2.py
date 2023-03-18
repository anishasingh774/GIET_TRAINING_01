"""Input: a string of comma seperated numbers. The number 5 and 8 are present in the list.Assume that 8 always comes after 5.
case1: num1= add all the numbers which do not lie between 5 and 8 in the input
case2: num2= number formed by concatenating all numbers from 5 to 8
output: sum of num1 and num2
1. 3,2,6,5,1,4,8,9
num1=3+2+6+9=20
num2=5148
o/p=5148+20=5168
"""

array=list(map(int,input().split(",")))
num1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
num2=""
for i in l:
     num2+=str(i)
print(int(num2)+num1)
print(num1)
print(num2)

