'''
DAY1: Python program to interchange first and last elements in a list by swaping the first element with (n-1)th element.
'''

# Define myList
myList = [29,8,98,15,5,10,6]

print('Input :',myList)

# copy firt element to temp
temp = myList[0]

# Swap (n-1)th element to first position
myList[0] = myList[-1]

# Update first element to (n-1)th position
myList[-1] = temp

print('Output :', myList)