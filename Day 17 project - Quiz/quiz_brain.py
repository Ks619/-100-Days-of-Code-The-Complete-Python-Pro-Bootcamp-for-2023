class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        """Returns True if there is more questions in the list, else returns False"""
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        """Calls to check_answer and moves to the next question"""
        user_answer = input(
            f"Q{self.question_number + 1}: {self.question_list[self.question_number].text} (True\\False)?:")
        self.check_answer(user_answer)
        self.question_number += 1

    def check_answer(self, user_answer):
        """Checks if the user's answer is correct"""
        if user_answer.lower() == self.question_list[self.question_number].answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was:{self.question_list[self.question_number].answer}.")
        print(f"Your correnut score is: {self.score}/{self.question_number}")
        print()
