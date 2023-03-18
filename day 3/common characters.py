"""Write a python program to display all the common characters between two strings.Return -1 if there are no matching characters.
note:Ignore blank spaces if there are any.
Perform case sensitive string comparison wherever necessary. 
i/p:                                                  o/p:
"I like Python"                                     lieyon
"Java is a very popular language"
"""
n="I like Python"
m="Java is a very popular language"
ans=""
for i in n:
     if i==" ":
         continue
     for j in m:
         if (i==j and j not in ans):
             ans+=i
print(ans)
