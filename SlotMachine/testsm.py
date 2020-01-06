from random import *

wheel_1 = ""
wheel_2 = ""
wheel_3 = ""
stash = 50


def one_armed_bandit():


   print("\nThe One Armed Bandit Welcome You")
   print("You have $ ", stash, " Would you like to play (y/n)?")
   choice = input()

   while choice == "y":
      spin_wheel()

   else:
    print("Goodbye! Come play again!")
    # one_armed_bandit()

    # Simulate the random spinning of the three wheels, print the result of the spins,
    # and determine the resulting payoff. Return the payoff amount
def spin_wheel():


  # global wheel_1, wheel_2, wheel_3, stash
   win = 0
   if stash <= 0:
      print("You are out of money. Come again soon.")
   while stash > 0:
      choice_bet = input("\n Type 'y' to play again or 'n' to quit: ")
      if choice_bet == "y":
         stash -= 1
      else:
         spin_wheel()

   if stash >= 0:
       stash -=1
   
       wheel1 = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR"]
       wheel2 = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR"]
       wheel3 = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR"]
       wheel_1 = choice(wheel1-1)
       wheel_2 = choice(wheel2-1)
       wheel_3 = choice(wheel3-1)


   if (wheel_1 == "CHERRY" and wheel_2 == "LEMON"):
        win = 2
        stash = stash + 2
   elif((wheel_1 == "CHERRY") and (wheel_2 == "CHERRY") and (wheel_3 != "CHERRY")):
        win = 5
        stash = stash + 5
   elif((wheel_1 == "CHERRY") and (wheel_2 == "CHERRY") and (wheel_3 == "CHERRY")):
        win = 7
        stash = stash + 7
   elif((wheel_1 == "ORANGE") and (wheel_2 == "ORANGE") and ((wheel_3 == "ORANGE") or (wheel_3 == "BAR"))):
        win = 10
        stash = stash + 10
   elif((wheel_1 == "PLUM") and (wheel_2 == "PLUM") and ((wheel_3 == "PLUM") or (wheel_3 == "BAR"))):
        win = 14
        stash = stash + 14
   elif((wheel_1 == "BELL") and (wheel_2 == "BELL") and ((wheel_3 == "BELL") or (wheel_3 == "BAR"))):
        win = 20
        stash = stash + 20
   elif((wheel_1 == "BAR") and (wheel_2 == "BAR") and (wheel_3 == "BAR")):
        win = 250
        stash = stash + 250
   
   else:
        win = -1
        stash = stash - 1

   print (wheel_1 + wheel_2 + wheel_3 + "You win " + win)