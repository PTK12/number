import random

number = random.randint(1,10)
tries = 3

print("I have a number between 1 and 10. Can you guess what it is?")

while tries > 0:

  while True:
    try:
      guess = int(input("The amount of guesses you have is " + str(tries) + "\n"))
      break

    except:
      print("Please enter a number!")
  
  if guess == number:
    print("You win!")
    break
  
  else:
    tries -= 1
    
    if tries == 0:
      print("Sorry! You lose")
      break
      
