#make a file with the responses
#create a randomizer
#make it respond to questions
#use a text file created
#the file should be put into a list
#prompt the user to ask a yes/no type question
#randomly display responses
#program repeats until user is ready to quit

#importing random to randomize answers

#create list of responses
def listResponses():
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]


    #create file in python
    with open("8ball_responses.txt", "w") as file:
        for response in responses:
            file.write(response + "\n")

#randomize responses
import random

def responses():
    with open("8ball_responses.txt", "r") as f:
        answers = f.read()  # read in text as string
        answers = answers.splitlines(True) #split the list

#ask a question and repeat until user enters 'N'
    question = input("Ask a question or enter \"N\" to quit: ")
    while not (question.upper().startswith("N")):
        print(random.choice(answers))
        question = input("\nAsk a question or enter \"N\" to quit: ")

#play the code
def main():
    responses()

if __name__ == "__main__":
    main()