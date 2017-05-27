from tkinter import Tk, Label, Button, LEFT, RIGHT, StringVar, IntVar, Entry
import pickle 
import random
import os
import string
from my_jeopardy import *

with open("wrds.pkl", 'rb') as qs:
    questions = pickle.load(qs)

class JepGui(object):
	def __init__(self, master, questions):

		# the title and params
		self.master = master
		master.title("Jeopardy! - Word Game")
		master.minsize(width=666, height=406)

		# define questions
		self.questions = random.sample(questions, len(questions))
		self.idx = 0
		self.q = self.questions[self.idx]


		# set score and points
		self.player_score = 0

		# set answers
		self.player_answer = StringVar()


		# the first label
		self.label = Label(master, text="This is JEOPARDY! - WORD GAMES \n", )
		self.label.pack()

		# the categories
		self.cat_text = StringVar()
		self.current_cat = self.q.category
		self.cat_text.set(self.current_cat)
		self.cat_label = Label(master, textvariable=self.cat_text)
		self.cat_label.pack()


		# the questions
		self.question_text = StringVar()
		self.current_question = self.q.question
		self.question_text.set(self.current_question)
		self.question_label = Label(master, textvariable=self.question_text)
		self.question_label.pack()

		# the question points
		self.points_text = StringVar()
		self.current_question_points = self.q.value
		self.points_text.set(self.current_question_points)
		self.points_label = Label(master, textvariable=self.points_text)
		self.points_label.pack()

		# create space for entry validation
		vcmd = master.register(self.validate)
		self.ent = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
		self.ent.pack()

		# submit button
		self.submit_button = Button(master, text='Pay me!')
		self.submit_button.bind("<Button-1>", self.submit_answer)
		self.submit_button.pack()

		# waiting for your answer
		self.messaged = "Waiting for your answer"
		self.labeled_text = StringVar()
		self.labeled_text.set(self.messaged)
		self.labeled = Label(master, textvariable = self.labeled_text)
		self.labeled.pack()


		# the next button
		self.next = Button(master, text='-->')
		self.next.bind("<Button-1>", self.cycle_questions)
		self.next.pack()

		# the player score
		self.score_text = StringVar()
		sc_text = "Player Score: " + str(self.player_score)
		self.score_text.set(sc_text)
		self.score_label = Label(master, textvariable = self.score_text)
		self.score_label.pack()


	def cycle_questions(self, event):
			self.idx+=1
			self.q = self.questions[self.idx]

			# change the category and question and points
			self.current_question = self.q.question
			self.current_cat = self.q.category
			self.current_question_points = self.q.value
			self.correct_response = self.q.answer

			# change the question and category text
			self.question_text.set(self.current_question)
			self.cat_text.set(self.current_cat)
			self.points_text.set(self.current_question_points)

			# reset label
			self.messaged = 'Waiting for your answer'
			self.labeled_text.set(self.messaged)




	def submit_answer(self, event):
		player_answer = self.ent.get()
		self.messaged = 'Waiting for your answer'
		if player_answer in self.q.answer:
			# answer text
			self.messaged = "Congrats! The correct answer is: " + self.q.answer
			self.labeled_text.set(self.messaged)

			#changing score
			self.player_score += self.current_question_points
			sc_text = "Player Score: " + str(self.player_score)
			self.score_text.set(sc_text)

		else: 
			# answer text field
			self.messaged = "Nope, the correct answer is: " + self.q.answer
			self.labeled_text.set(self.messaged)

			# changing score
			self.player_score -= self.current_question_points
			sc_text = "Player Score: " + str(self.player_score)
			self.score_text.set(sc_text)

	def validate(self, new_text):
		if not new_text:
			self.player_answer = None
			return True

		try:
			guess = str(new_text)
			return True

		except ValueError:
			return False
		
				







root = Tk()
gui = JepGui(root, questions)
root.mainloop()