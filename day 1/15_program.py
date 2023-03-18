"""Write a python function to add 'ing' at the end of a given string and return the new string.
If the given string already ends with 'ing' then add 'ly' .
If the length of the given string is < 3 leave it unchanged.

Sample Input       Expected Output
sleep                 sleeping
amazing               amazing
is                      is    """


def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('sleep'))
print(add_string('amazing'))
print(add_string('is'))

