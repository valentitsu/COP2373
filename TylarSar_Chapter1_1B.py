#create a randomizer
#make it respond to questions
#use a text file created
#the file should be put into a list
#prompt the user to ask a yes/no type question
#randomly display responses
#program repeats until user is ready to quit

#importing random to randomize answers
import random
#opens the 8ball file and reads it
with open("eight_ball_responses.txt", "r") as f:
    answers = f.read()

#separates the lines so questions will be replied to with one response
answers = answers.strip().splitlines(True)

#ask a question, wait for user input, repeat until user enters 'N'
question = input("Ask a question or enter \"N\" to quit: ")
while not(question.upper().startswith("N")):
    #while statement loops the code until 'N' is entered

    print(random.choice(answers))
    question = input("\nAsk a question or enter \"N\" to quit: ") #code repeats










