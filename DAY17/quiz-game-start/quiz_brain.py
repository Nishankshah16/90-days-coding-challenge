class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def still_has_ques(self):
        return self.question_number <  len(self.question_list)


    def next_question(self):
        current_question= self.question_list[self.question_number]
        self.question_number+=1
        user_input=input(f"Q{self.question_number}{current_question.text}").lower()
        self.check_answer(user_input,current_question.answer)

    def check_answer(self, user_input, current_question):
        if user_input==current_question.lower():
            print("You are right")
            self.score+=1
        else:
            print("You are wrong")
        print(f"The correct answer is {current_question}")
        print(f"Your score is {self.score}/{self.question_number}")

        print("\n")
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       

