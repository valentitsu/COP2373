# Any number of sentences, including sentences which begin with numbers. Display count of sentences after.

import re

def main():
    # User's sentences
    sentences = []

    # Prompt user to enter any amount of sentences
    print("Enter sentences (type 'done' to end):")

    while True:
        #Take input from the user
        sentence = input()

        #Add quit for the user when user ready to end
        if sentence.lower() == 'done':
            break

        sentences.append(sentence)

    # Show sentences
    print("\nThese are the sentences inputted:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")

    # Number the sentence(s)
    print(f"\nAmount of sentences you inputted: {len(sentences)}")

if __name__ == "__main__":
    main()