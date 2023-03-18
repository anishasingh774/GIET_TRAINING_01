mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop --odd -->square it
#even-->cube it


result = []

for row in mat:
    row_data = []
    for element in row:
        if element % 2!=0:
            row_data.append(element ** 3)
        else:
            row_data.append(element ** 2)
    result.append(row_data)
print(result)
# list comprehension
print([element**2 if element%2!=0 else element**3 for row in mat for element in row])

print([[element**2 if element%2!=0 else element**3  for element in row] for row in mat])
