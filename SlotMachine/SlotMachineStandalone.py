import random

def slot_machine_out():

    current_stash = 50
    print(" ")
    print("          The Slot-Machine Says Hello!!")
    print("          -----------------------------")
    print(" ")
    print("You have $", current_stash, ".", sep="", end=" ")
    answer = input("Would you like to play (y/n)? ")
    while (current_stash > 0 and  answer[0] == 'y'):
        payoff = slot_wheel()
        current_stash = current_stash - 1 + payoff
        if (current_stash == 0):
            print("You have $", current_stash, ".", sep="", end=" ")
            answer = input("Would you like to play (y/n)? ")
    if (current_stash == 0):
        print("Sorry, the slot machine requires 1 token! Please come again.")
    else:
        print("Bye! Play again soon!")

def slot_wheel():

    spin_symbol = ["CHERRY", "GRAPE", "LEMON", "SEVEN", "BELL", "BAR"]
    spin1 = random.randint(1, 6)
    spin2 = random.randint(1, 6)
    spin3 = random.randint(1, 6)
    symbol1 = spin_symbol[spin1-1]
    symbol2 = spin_symbol[spin2-1]
    symbol3 = spin_symbol[spin3-1]
    print(symbol1, "     ", end="")
    print(symbol2, "     ", end="")
    print(symbol3, " -- ", end="")


    payoff = 0
    if (symbol1 == "SEVEN" and symbol2 == "SEVEN" and symbol3 == "SEVEN"):
        payoff = 250
    elif (symbol1 == "BAR" and symbol2 == "BAR" and (symbol3 == "BAR" or symbol3 == "SEVEN")):
        payoff = 20
    elif (symbol1 == "BELL" and symbol2 == "BELL" and (symbol3 == "BELL" or symbol3 == "SEVEN")):
        payoff = 14
    elif (symbol1 == "GRAPE" and symbol2 == "GRAPE" and (symbol3 == "GRAPE" or symbol3 == "SEVEN")):
        payoff = 10
    elif (symbol1 == "CHERRY" and symbol2 == "CHERRY" and symbol3 == "CHERRY"):
        payoff = 7
    elif (symbol1 == "CHERRY" and symbol2 == "CHERRY"):
        payoff = 5
    elif (symbol1 == "CHERRY"):
        payoff = 0

    if (payoff == 0):
        print("You lose")
    else:
        print("You win $", payoff, sep="")

    print(" ")

    return payoff  