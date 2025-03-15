# https://opentdb.com/      --trivia DB

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questionbank=[]

for i in question_data:
    question_text=i["text"]
    question_answer=i["answer"]
    a=Question(question_text,question_answer)
    questionbank.append(a)

quizBrain = QuizBrain(questionbank)
while quizBrain.still_has_ques():
    quizBrain.next_question()

print("Congratulations!! You have completed the quiz.")
print(f"Your score is {quizBrain.score}/{quizBrain.question_number}")
