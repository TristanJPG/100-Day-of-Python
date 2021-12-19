class QuizBrain: 
    def __init__(self, q_list):
        self.q_num = 0
        self.question_list = q_list
        self.score = 0
    def still_has_question(self):
       return self.q_num < len(self.question_list)
         
    def next_question(self):
        current_question = self.question_list[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q.{self.q_num}: {current_question.text} (True or False) ")
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score += 1
            print("Correct! :D")
        else:
            print("That's wrong! :(")
        print(f"The correct answer is {correctAnswer}. ")
        print(f"Your Score is {self.score}/{self.q_num}. ")
        print("\n")