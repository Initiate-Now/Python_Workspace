'''*****************************************************
* Name     : ListOfFruit.py
* Category : Lists - Creating, Accessing, Modifying, 
             and Basic List Operations.
* Program  : Write a Python function that creates a list of your
             favorite fruits. Add a new fruit to the list 
             and then print each fruit in the list.
* Author   : Navin Chakravarthy Kamalakannan
*********************************************************'''
def favorite_fruits():
    # create a list of favorite fruits
    fruits = ["Mango", "Banana", "Strawberry", "Apple"]

    # Add a new fruit to the list
    fruits.append("Pineapple")

    # Print each fruit in the list
    print("My favorite fruits are:")
    for fruit in fruits:
        print(fruit)

# Call the function
favorite_fruits()