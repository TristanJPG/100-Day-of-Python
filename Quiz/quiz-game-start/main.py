from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
scorePercent = ((quiz.score) / (quiz.q_num)) * 100

print("The quiz is completed!")
print(f"Your final score was {str(int(scorePercent))}%")






