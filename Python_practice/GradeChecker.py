'''*****************************************************
* Name     : GradeChecker.py
* Category : Control Flow - Conditional Statements (if, elif, else).
* Program  : Write a Python script that takes a student's grade
             as input (A,B,C,D,or F) and prints a corresponding message 
             (e.g., "Excellent","Good Job!", etc.).
* Author   : Navin Chakravarthy Kamalakannan
*********************************************************'''
# Prompt the user to enter the student's grade
grade = input("Enter the student's grade (A,B,C,D,or F): ").upper()

# Define messages for each grade
grade_messages = {
    "A" : "Excellent!",
    "B" : "Good Job!",
    "C" : "Well Done!",
    "D" : "You Passed.",
    "F" : "Better Luck Next Time."
}

# Get the message based on grade and print it
print(grade_messages.get(grade, "Invalid grade entered."))