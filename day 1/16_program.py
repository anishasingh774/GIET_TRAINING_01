"""Write a python function,check_double(number) which accepts a whole number and
returns True if it satisfies the given conditions.
1. The number and its double should have exactly the same number of digits.
2. Both the numbers should have the same digits but in otherwise it should return false.

Example: If the number is 125874 and its double , 251748, contain exactly the same digits, but in a different order.  """



def check_double(number):
    num1=str(number*2)
    number=str(number)
    count=0
    for x in number:
        if x in num1:
            count+=1
        else:
            return False
            break
    if count==len(number):
        return True
print(check_double(125874))

