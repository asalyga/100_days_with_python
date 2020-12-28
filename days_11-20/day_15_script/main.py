from question_model import Question
from data import question_data
from quiz_brain import quiz_brain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = quiz_brain(question_bank)

while quiz.questions_left():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")