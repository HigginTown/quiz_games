import pickle
import random

class Question(object):
    def __init__(self, category, question, answer, value):
        self.category = category
        self.question = question
        self.answer = answer
        self.value = value 
 
    def ask(self):
        # category
        category_text = ("Category: \n ", self.category)
        print(category_text)

        # question
        question_text = str(self.question)
        print ("\n", question_text)
        response = input("Your answer: ").strip()
        if response in self.answer:
            print("Correct!")
            return(self.value)
        else: 
            print("Wrong! \n")
            print("Answer is: ", self.answer)
        return(-self.value)
   
class Jeopardy(object):
    def __init__(self, questions, score=0):
        self.questions = random.sample(questions, len(questions))
        self.score = score
        
    def play(self):

        for question in self.questions:
            print("Press a key")
            player_action = str(input())
            if player_action in ["quit", "no", "exit", "escape", "leave", "stop"]:
                break
            self.score+=question.ask()
            print("Score is: ",  self.score)
            print("Continue?")

    def filter(self, filter_terms):
        print("Filters are:", filter_terms)
        filtered_questions = []
        for q in self.questions:
            for term in filter_terms:
                if (term in q.question) or (term in q.answer) or (term in q.category):
                    filtered_questions.append(q)

        if len(filtered_questions)>0:
            print("Filtered questions: ", len(filtered_questions))
            self.questions = filtered_questions
        else:
            return 0
            print("No matches!")

        
        
        