# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it in 10 attemps and the computer 
# lets the player know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 10 attempts.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while (tries < 10) and (guess != the_number):
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
            
    guess = int(input("Take a guess: "))
    tries += 1

if guess == the_number:
   print("\nYou guessed it!  The number was", the_number)
   print("\nAnd it only took you", tries, "tries!\n")
else:
   print("\nYou did not guess it!  The number was", the_number)
   print("\nIt took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
