# Buyer: Max 4 tickets
# 20 tickets available
# Prompt buyer desired number of tickets
# Display remaining tickets after purchase
# Repeat until 0 tickets.
# Display total buyers.

#define variables
def ticketBooth():
    ticketsAvailable = 20
    buyers = 0

#loop until all tickets are sold and add user input.
    while ticketsAvailable > 0:
        print("Tickets available ", ticketsAvailable)
        purchasedTickets = int(input("Desired number of tickets (max 4): "))

#if statements are for constraints if the user enters 0 or negative numbers, more than 4 tickets,
#or more than the available tickets (these are in order)
        if purchasedTickets <= 0:
            print("You cannot purchase 0 tickets.")
            continue
        if purchasedTickets > 4:
            print("You cannot purchase over 4 tickets.")
            continue
        if purchasedTickets > ticketsAvailable:
            print("Available tickets is lower than the amount desired to buy.")
            continue

#the total tickets available subtracted by purchased tickets, add the total buyers.
        ticketsAvailable -= purchasedTickets
        buyers += 1

#display the total buyers at the end
    print("Total buyers ", buyers)

def main():
    ticketBooth()

if __name__ == "__main__":
    main()






