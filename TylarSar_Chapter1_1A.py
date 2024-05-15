# Buyer: Max 4 tickets
# 20 tickets available
# Prompt buyer desired number of tickets
# Display remaining tickets after purchase
# Repeat until 0 tickets.
# Display total buyers.

def ticketBooth():
    ticketsAvailable = 20
    buyers = 0

    while ticketsAvailable > 0:
        print("Tickets available ", ticketsAvailable)
        purchasedTickets = int(input("Desired number of tickets (max 4) "))


        if purchasedTickets <= 0:
            continue
        if purchasedTickets > 4:
            continue
        if purchasedTickets > ticketsAvailable:
            continue

        ticketsAvailable -= purchasedTickets
        buyers += 1

    print("Total buyers ", buyers)

def main():
    ticketBooth()

if __name__ == "__main__":
    main()






