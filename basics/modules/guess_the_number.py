


def play_guess_the_number():
  import random as rnd
  print("-----------------------------")
  print("\n")
  print("Welcome to the guessing game. \n")
  print("\n")
  print("-----------------------------")
  print("\n")
  print("Please enter the minimum value:")
  m = int(input())
  print("Please enter the maximum value:")
  M = int(input())

  print(f"I am thinking of a number between {m} and {M}.  Can you guess what it is?")
  x = rnd.randrange(m, M)
  guess = 0
  i = 1

  while i > 0:
    guess = int(input())
    if guess == x:
      print("\n")
      print("Congratulations! You guessed my number!")
      print("\n")
      i = 0
    elif guess < x:
      print("Your guess is too low.")
      print("Try again:")
      
    elif guess > x:
      print("Your guess is too high.")
      print("Try again:")
  
  print("\n")
  print("*******************")
  print("You win. Game over!")
  print("*******************")
  print("\n")
    

play_guess_the_number()
