'''*****************************************************
* Name     : NumberOfVowels.py
* Category : Strings - Creating, Accessing, Slicing, and
             Common String Methods.
* Program  : Write a Python script that takes a sentence as input
             and counts the number of vowels (a,e,i,o,u) in it.
* Author   : Navin Chakravarthy Kamalakannan
*********************************************************'''
# Get input from user
sentence = input("Enter a sentence: ")

# Define vowels
vowels = "aeiouAEIOU"
count = 0

# Loop through each character in the sentence
for char in sentence:
    if char in vowels:
        count += 1

# Display the result
print(f"Number of vowels in the sentence: {count}")