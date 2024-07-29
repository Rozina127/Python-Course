# some naming convention in python 
#   01. pascal case    all the starting letters in name is capitilized like PascalCase
#   02. camelcase  starting letters in name is small like camelCase
#   03. snake case    all the name is separated by underscore like snake_case 

class user:
    pass 
    
    
user1=user()
user1.id=123
user1.name="Rozina"

print(user1.id)
print(user1.name)

user2=user()

user2.id=456
user2.name="Wali"

print(user2.id)
print(user2.name)



# The above task is complex to print name and id of each user one by one for this problem we use constructor 

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

user1 = User(123, "Rozina")
user2 = User(456, "Wali")

print(f"ID: {user1.id}, Name: {user1.name}")  # Output: ID: 123, Name: Rozina
print(f"ID: {user2.id}, Name: {user2.name}")  # Output: ID: 456, Name: Wali
 
 
#using methods 
# Class to represent a single question and its answer
class Question:
    def __init__(self, text, answer):
        # Initialize the question text and the correct answer
        self.text = text
        self.answer = answer

# Class to manage the quiz functionality
class Quiz:
    def __init__(self, questions):
        # Initialize the quiz with a list of Question objects
        self.questions = questions
        self.score = 0  # Initialize score to 0
        self.question_number = 0  # Initialize question number to 0

    def next_question(self):
        # Retrieve the current question from the list
        current_question = self.questions[self.question_number]
        # Increment the question number for the next call
        self.question_number += 1
        # Prompt the user for their answer
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        # Check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # Compare user's answer with the correct answer
        if user_answer.lower() == str(correct_answer).lower():
            self.score += 1  # Increment the score if the answer is correct
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {correct_answer}.\n")

    def has_more_questions(self):
        # Check if there are more questions to ask 
        return self.question_number < len(self.questions)

    def show_final_score(self):
        # Display the final score at the end of the quiz
        print(f"Your final score is {self.score}/{len(self.questions)}")

def main():
    # List of Question objects with text and correct answers
    question_data = [
        Question("The sky is blue.", True),
        Question("The sum of 2 and 2 is 5.", False),
        Question("Python is a programming language.", True),
        Question("The Earth is flat.", False),
        Question("Water boils at 100 degrees Celsius.", True)
    ]

    # Create a Quiz object with the list of questions
    quiz = Quiz(question_data)

    # Loop through and ask each question until there are no more questions
    while quiz.has_more_questions():
        quiz.next_question()

    # Show the final score once the quiz is complete
    quiz.show_final_score()

# main function if this script is execute
if __name__ == "__main__":
    main()
