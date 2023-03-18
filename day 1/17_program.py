""" A teacher is in the process of generating few reports based on the marks scored by the students of her class in a
project in assessment.
Assume that the marksof her 10 students are available in a tuple, the marks are out of 25.
Write a python program to implement the following functions:
1. find_more_than_average(): Find and return the percentage of students who have scored more than the average 
mark of the class.OverflowError
2. generate_frequency() : find how many students have scored the same works. The results should be populated in a 
listand returned.
3. sort_marks() : Sort the marks in the increasing order from 0 to 25. The sorted values should be populated in a
list and returned """


list_of_marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average():
    marks=0
    count=0
    for x in list_of_marks:
        marks+=x
    average=marks/len(list_of_marks)
    for x in list_of_marks:
        if x>average:
            count+=1
    percentage=(count*100)/len(list_of_marks)
    return percentage
def generate_frequency():
    freq=[]
    for x in range(26):
        count=0
        for y in list_of_marks:
            if x == y:
                count+=1
        freq.append(count)
    return  freq
def sort_marks():
    list_of_marks=sorted(list_of_marks)
    return list_of_marks

print(find_more_than_average())
print(generate_frequency()) 
print(sort_marks())
