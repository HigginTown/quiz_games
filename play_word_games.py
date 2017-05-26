from my_jeopardy import Jeopardy, Question
import pickle
import random
import string
import os

print("\n Welcome to your personal Jeopardy! - Word Games \n")
print("Press any key for a new question, or 'quit' to exit")

with open("wrds.pkl", 'rb') as qs:
    questions = pickle.load(qs)

game = Jeopardy(questions[:])


# print("\n Would you like to filter your questions? [y/n]")
# answer = input()
# if answer in ["yes", 'Yes', 'Y', 'y']:
# 	print('Enter your filter terms, seprated by a comma: ')
# 	filters = list(map( str, input().split(',')))
# 	for f in filters:
# 		f = f.lower()
# 	l = game.filter(filters)
# 	if l == 0:
# 		print("Try again!")
# 		filters = list(map( str, input().split(',')))
# 		game.filter(filters)

# 	print("Filter complete, let's play!")

game.play()

