# Any number of sentences, including sentences which begin with numbers. Display count of sentences after.

import re

def main():
    # Prompt user to enter sentences, then press enter when done.
    s = input("Enter sentences. Press ENTER when done.\n")
    # Allows for sentence creation.
    pat = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    m = re.findall(pat, s, flags=re.DOTALL | re.MULTILINE)

# Start sentence counter at 0
    counter = 0

    # Display and count sentences
    for i in m:
        counter+=1
        print('->', i)
    print(f'Total Sentences:', counter)

if __name__ == "__main__":
    main()