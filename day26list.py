numbers = [1, 2, 3]
new_list = []

# Using a for loop (commented out)
"""
for n in numbers:
    new_item = n + 2
    new_list.append(new_item)
print(new_list)
"""

# Using list comprehension to add 2 to each number in the list
new_list = [n + 2 for n in numbers]
print(new_list)  # Output: [3, 4, 5]

# Using string
name = "Rozina"

# Using list comprehension to create a list of characters from the string
char_list = [char for char in name]
print(char_list)  # Output: ['R', 'o', 'z', 'i', 'n', 'a']

# More examples of list comprehensions

# Squaring each number in the list
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)  # Output: [1, 4, 9]

# Creating a list of even numbers from the original list
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # Output: [2]

# Creating a list of numbers greater than 1 from the original list
numbers_greater_than_one = [n for n in numbers if n > 1]
print(numbers_greater_than_one)  # Output: [2, 3]

# Converting each character in the name to uppercase
uppercase_chars = [char.upper() for char in name]
print(uppercase_chars)  # Output: ['R', 'O', 'Z', 'I', 'N', 'A']

# Combining elements from two lists using list comprehension
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [(x, y) for x in list1 for y in list2]
print(combined_list)  # Output: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

#dictionary com
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [95, 82, 78, 90]
}

# Creating a dictionary with names as keys and scores as values
name_score_dict = {data['Name'][i]: data['Score'][i] for i in range(len(data['Name']))}
print(name_score_dict)  # Output: {'Alice': 95, 'Bob': 82, 'Charlie': 78, 'David': 90}

# Creating a dictionary with names as keys and a boolean indicating if the score is above 80
above_80_dict = {data['Name'][i]: data['Score'][i] > 80 for i in range(len(data['Name']))}
print(above_80_dict)  # Output: {'Alice': True, 'Bob': True, 'Charlie': False, 'David': True}

# Creating a dictionary with names as keys and the length of each name as values
name_length_dict = {name: len(name) for name in data['Name']}
print(name_length_dict)  # Output: {'Alice': 5, 'Bob': 3, 'Charlie': 7, 'David': 5}

# Creating a dictionary with scores as keys and names as values (assuming unique scores)
score_name_dict = {data['Score'][i]: data['Name'][i] for i in range(len(data['Score']))}
print(score_name_dict)  # Output: {95: 'Alice', 82: 'Bob', 78: 'Charlie', 90: 'David'}

# Creating a dictionary with names as keys and a message as values
message_dict = {name: f"{name} scored {score}" for name, score in zip(data['Name'], data['Score'])}
print(message_dict)  # Output: {'Alice': 'Alice scored 95', 'Bob': 'Bob scored 82', 'Charlie': 'Charlie scored 78', 'David': 'David scored 90'}







#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as List
name = "Angela"
letters_list = [letter for letter in name]

#Range as List
range_list = [n * 2 for n in range(1, 5)]

#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)