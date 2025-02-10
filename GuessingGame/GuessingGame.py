print("Welcome, and thanks for playing my Guessing Game!")
print("The rules to this game are simple, guess a number between 1 and 10. If you guess too high or too low I'll let you know")
import random
number = random.randint(1,10)
PlayerGuess = 0
while PlayerGuess != number:
      PlayerGuess = int(input("What's my favorite number?"))
      if (PlayerGuess < number):
            print("Too low! Try again.")
      elif (PlayerGuess > number):
            print("Too high! Try again.")
      else:
          print("How'd you know! Good job!")
print("Would you like to play again? enter y for yes, or n for no. ")
if "y": 
        print("Welcome, and thanks for playing my Guessing Game!")
        print("The rules to this game are simple, guess a number between 1 and 10. If you guess too high or too low I'll let you know")
        import random
        number = random.randint(1,10)
        PlayerGuess = 0
while PlayerGuess != number:
        PlayerGuess = int(input("What's my favorite number?"))
        if (PlayerGuess < number):
            print("Too low! Try again.")
        elif (PlayerGuess > number):
            print("Too high! Try again.")
        else:
          print("How'd you know! Good job!")
        print("Would you like to play again? enter y for yes, or n for no.")
if "n":
     print("thanks for playing!")
        
      