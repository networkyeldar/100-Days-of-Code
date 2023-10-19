class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} True or False?:")
        if user_answer == current_question.answer:
            print("You got it right!")
            print(f"The correct answer was {current_question.answer}")
            self.score += 1
        else:
            print("You made a mistake")
            print(f"The correct answer was {current_question.answer}")
        print(f"You score is {self.score} out of {self.question_number}")
