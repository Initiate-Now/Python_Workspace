'''*****************************************************
* Name     : AverageOfList.py
* Category : Functions - Defining functions using def,
             arguments, Return Values.
* Program  : Write a Python function that takes a list of
             numbers as input and returns the average of those
             numbers.
* Author   : Navin Chakravarthy Kamalakannan
*********************************************************'''
def calculate_average(numbers):
    if not numbers:
        return 0 # Return 0 if the list is empty to avoid division by zero
    return sum(numbers)/len(numbers)

# Example usage
num_list = [10,20,30,40,50]
average = calculate_average(num_list)
print("Average:", average)