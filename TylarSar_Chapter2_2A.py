#Find common 30 words and phrases commonly found in spam email, then write a list of those 30
#Tell user to write their email
#scan the messages and add to a list
#add spam score for every common phrase or word
#rate the liklihood that the message is a spam
#display user's score

import re

#Define a list of common spam keywords
def spamWords():
    return [
        "#1", "100% more", "100% free", "100% satisfied", "Additional income", "Be your own boss",
        "Best price", "Big bucks", "Billion", "Cash Bonus", "Cents on the dollar", "Consolidate debt",
        "Double your cash", "Earn extra cash", "Earn Money", "Eliminate bad credit", "Extra cash", "Extra income",
        "Expect to earn", "Fast cash", "Financial freedom", "Free access", "Free consultation", "Free gift",
        "Free hosting", "Free info", "Free investment", "Free membership", "Free money"
    ]


#Function to calculate the spam score. Defines score as 1.
def scoreCalc(email_message, keywords):
    score = 0
    detected_keywords = []
    email_message_lower = email_message.lower()

#Search the email for keywords, can be lowercase as well as uppercase. For every 1 keyword or phrase in the email, add one point to the score.
    for keyword in keywords:
        keyword_pattern = re.escape(keyword.lower())
        if re.search(keyword_pattern, email_message_lower):
            score += 1
            detected_keywords.append(keyword)

    return score, detected_keywords


#Function to determine the likelihood of spam based on the score.
#The score will determine the likeliness of the email being a scam according to how many keywords have been present.
def spamLikelihood(score):
    if score == 0:
        return "Not a Spam Message"
    elif score <= 5:
        return "Low chance of Spam"
    elif score <= 10:
        return "Medium chance of Spam"
    elif score <= 15:
        return "High chance of Spam"
    else:
        return "Most likely Spam"
#Any points past 15 will be flagged


#Main function to get user input, print results of the email sent by the user, rate the likelihood of spam, and note the words and phrases that were present.
def main():
    email_message = input("Enter the email message: ")
    spam_keywords = spamWords()
    score, detected_keywords = scoreCalc(email_message, spam_keywords)
    likelihood = spamLikelihood(score)

    print("\nSpam Analysis Results:")
    print(f"Spam Score: {score}")
    print(f"Likelihood of Spam: {likelihood}")

#If statement is used to print either detected keywords (prints all present words and phrases and puts it in a list) or no keywords.
    if detected_keywords:
        print(f"Detected Spam Keywords/Phrases: {', '.join(detected_keywords)}")
    else:
        print("No spam keywords/phrases detected.")


#Run the main function
if __name__ == "__main__":
    main()