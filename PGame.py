import sys
import subprocess
import time
import random

try:
    from termcolor import colored
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "termcolor"])
    from termcolor import colored

lessons = [
    {
        "topic": "Variables",
        "text": "A variable in Python is a container to store a value. You can assign a value to a variable using the equal sign (=). Variables can store different types of data like integers, floats, strings, or booleans. For example, 'x = 5' assigns the value 5 to the variable x, and 'name = \"John\"' assigns the string 'John' to the variable name.",
        "questions": [
            {
                "text": "What is the correct syntax to assign a value to a variable?",
                "options": ["x 5", "x : 5", "x <- 5", "x = 5"],
                "answer": 3
            },
            {
                "text": "Which character is used to assign a value to a variable?",
                "options": [":", "=", "<-", "->"],
                "answer": 1
            },
            {
                "text": "What is the output of the following code? \n\nx = 5\ny = 3\nprint(x + y)",
                "options": ["53", "8", "xy", "Error"],
                "answer": 1
            },
        ],
    },
    {
        "topic": "Data Types",
        "text": "Python has several built-in data types, such as strings (str), integers (int), floating point numbers (float), and booleans (bool). Strings are sequences of characters enclosed in quotes (e.g., 'Hello, World!'). Integers represent whole numbers (e.g., 42). Floating point numbers represent real numbers with decimal points (e.g., 3.14). Booleans represent True or False values.",
        "questions": [
            {
                "text": "Which of these is a string in Python?",
                "options": ['"Hello"', "42", "3.14", "True"],
                "answer": 0
            },
            {
                "text": "What is the data type of the value '5.0'?",
                "options": ["str", "int", "float", "bool"],
                "answer": 2
            },
            {
                "text": "Which of these is a boolean in Python?",
                "options": ['"True"', "1", "0", "False"],
                "answer": 3
            },
        ],
    },
    {
        "topic": "Lists",
        "text": "A list is a collection of items in Python. You can create a list using square brackets [], and items are separated by commas. Lists can store different types of data and can even include other lists. For example: my_list = [1, 2, 3], or nested_list = [[1, 2], [3, 4]]. You can access list items using their index (starting at 0) with my_list[index]. The len() function returns the length of a list.",
        "questions": [
            {
                "text": "How do you create an empty list?",
                "options": ["[]", "{}", "list()", "empty_list"],
                "answer": 0
            },
            {
                "text": "What is the output of the following code? \n\nmy_list = [1, 2, 3]\nprint(my_list[1])",
                "options": ["1", "2", "3", "Error"],
                "answer": 1
            },
            {
                "text": "What is the output of the following code? \n\nmy_list = [1, 2, 3]\nprint(len(my_list))",
                "options": ["1", "2", "3", "Error"],
                "answer": 2
            },
        ],
    },
    {
        "topic": "If Statements",
        "text": "An if statement is a control structure that allows you to conditionally execute a block of code. The syntax is 'if condition:'. The code inside the block will execute only if the condition is True. You can add more conditions using 'elif condition:' and provide a default block of code with 'else:'. Comparison operators like '==', '!=', '<', '>', '<=', and '>=' are often used in conditions.",
        "questions": [
            {
                "text": "What is the correct syntax for an if statement?",
                "options": ["if condition", "if condition:", "if (condition):", "if: condition"],
                "answer": 1
            },
            {
                "text": "Which of these is the correct way to check if a variable x is equal to 5?",
                "options": ["if x = 5", "if x == 5", "if x === 5", "if x == 5:"],
                "answer": 1
            },
            {
                "text": "Which keyword is used to check an additional condition if the previous condition is False?",
                "options": ["elif", "else", "else if", "elseif"],
                "answer": 0
            },
        ],
    },
]

def ask_question(question, index):
    print(colored(f"\nQuestion {index + 1}: {question['text']}", "red"))
    options = random.sample(question["options"], len(question["options"]))
    for i, option in enumerate(options):
        print(colored(f"{i + 1}. {option}", "red"))
    attempts = 0
    while attempts < 3:
        try:
            answer = int(input("Enter the number of your choice: ")) - 1
            if options[answer] == question["options"][question["answer"]]:
                print(colored("Correct!", "green"))
                return 2
            else:
                attempts += 1
                print(colored("Incorrect, try again.", "yellow"))
        except (ValueError, IndexError):
            attempts += 1
            print(colored("Invalid input, try again.", "yellow"))
    print(colored("Out of attempts, moving to the next question.", "yellow"))
    return 0

def main():
    score = 0
    for lesson in lessons:
        print(colored(f"\nLesson: {lesson['topic']}", "cyan"))
        print(colored(lesson["text"], "cyan"))
        time.sleep(1)
        for i, question in enumerate(lesson["questions"]):
            score += ask_question(question, i)
    print(colored(f"\nYour final score is {score} out of 24.", "cyan"))

if __name__ == "__main__":
    main()
