import random

number = random.randint(1,10)
tries = 3

guess = input("I have a number between 1 and 10. Can you guess what it is? You have 3 guesses! ")

answer = int(guess)

while tries > 0:
  if answer == number:
    print("You win!")
    break
  else:
    tries -= 1
    if tries == 0:
      print("Sorry! You lose")
      break
    else:
      input("Try again ")
    
