import random

card_list = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]*4

total = 100
print("Welcome to blackjack!")
print("You currently have: $" + str(total))
bet = input("How much do you want to bet? ")




def deal_player_hand():
    p_card_1 = random.choice(card_list)
    p_card_2 = random.choice(card_list)
    return p_card_1 and p_card_2


def calculate_player_hand():
    deal_player_hand()
    p_tally = 0
    if p_card_1 == "J" or p_card_1 == "Q" or p_card_1 == "K":
        p_tally += 10
    elif p_card_1 == "A":
        p_tally += 11
    else:
        p_tally += p_card_1

    if p_card_2 == "J" or p_card_2 == "Q" or p_card_2 == "K":
        p_tally += 10
    elif p_card_2 == "A":
        p_tally += 11
    else:
        p_tally += p_card_2

    return p_tally


def deal_dealer_hand():
    d_card_1 = random.choice(card_list)
    d_card_2 = random.choice(card_list)
    return d_card_1 and d_card_2
    
def calculate_dealer_hand():
    deal_dealer_hand()
    d_tally = 0
    if d_card_1 == "J" or d_card_1 == "Q" or d_card_1 == "K":
        d_tally += 10
    elif d_card_1 == "A":
        d_tally += 11
    else:
        d_tally += d_card_1

    if d_card_2 == "J" or d_card_2 == "Q" or d_card_2 == "K":
        d_tally += 10
    elif d_card_2 == "A":
        d_tally += 11
    else:
        d_tally += d_card_2

    return d_tally


def hit_player():
    p_card_temp = random.choice(card_list)
    if p_card_temp == "J" or p_card_temp == "Q" or p_card_temp == "K":
        p_tally += 10
    elif p_card_temp == "A":
        p_tally += 11
    return p_card_temp

def dealer_decision():
    if d_tally < 17:
        d_card_temp = random.choice(card_list)

    if d_card_temp == "J" or d_card_temp == "Q" or d_card_temp == "K":
        d_tally += 10
    elif d_card_temp == "A":
        d_tally += 11
    return d_tally


calculate_player_hand()
calculate_dealer_hand()

#Round 1

if p_tally == 21:
    print("You got a blackjack!")
    print("You currently have: $" + str(total + bet * 2))
elif d_tally == 21:
    print("The dealer got a blackjack!")
    print("You currently have: $" + str(total - bet))
else:
    print("Current hand: " + str(p_card_1) + " " + str(p_card_2))
    decision = input("Do you wish to hit or stand?").lower()
    if decision == "hit":
        print("hi")
        #round_1_p = hit_player()
        #dealer_decision()
    elif decision == "stand":
        print("bye")
        #dealer_decision()
    else:
        print("Invalid input")

#Round 2
        
if p_tally == 21:
    print("You got a blackjack!")
    print("You currently have: $" + str(total + bet * 2))
elif d_tally == 21:
    print("The dealer got a blackjack!")
    print("You currently have: $" + str(total - bet))
elif p_tally > 21:
    print("Bust!")
    print("You currently have: $" + str(total - bet))
elif d_tally > 21:
    print("The dealer bust!")
    print("You currently have: $" + str(total + bet * 2))
else:
    print("Current hand: " + str(p_card_1) + str(p_card_2) + str(round_1_p))
    decision = input("Do you wish to hit or stand?").lower()
    if decision == "hit":
        print("pee")
        #round_1_p = hit_player()
        #dealer_decision()
    elif decision == "stand":
        print("poop")
        #dealer_decision()
    else:
        print("Invalid input")
    

    
    







