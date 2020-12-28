class quiz_brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def questions_left(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False)?: ")
        self.answer_check(user_answer, current_q.answer)

    def answer_check(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong answer!")
            print(f"The correct answer was: {correct_answer}")
        print(f"You'r score is: {self.score}/{self.question_number}.\n")
