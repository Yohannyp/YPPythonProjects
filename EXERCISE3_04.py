# Guess My Number
#
# The user picks a random number between 1 and 100
# The computer tries to guess it and lets
# the player know.              
   
import random  

print("\tWelcome to 'The Computer Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")

# set the initial values
the_number = int(input("Pick a Random Number Between 1 and 100: "))
guess = 0
tries = 0

# guessing loop
while guess != the_number:
      guess =  random.randint(1, 100)
      print(guess) 
      tries += 1

print("The Computer guess it!  The number was", the_number)
print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
