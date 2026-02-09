# number guessing game
import random
number = random.randint(1,100)
print("Guuess number between 1 to 100.")
print("You have 7 attempts to guess the number!")
attempt = 7

while attempt > 0:
     try:
        guess = int(input("Enter your guess: ")) 
     except ValueError: 
          print("Your input is Invalid")
          continue
     if guess > number:
         print("Your guess is too High")
     elif guess < number:
         print("your guess is too Low")
     else:
        print(f"Amazing! You guessed it with {attempt} attempts left!")
        break

     attempt -= 1
     print(f"Attempt left: {attempt}")

if attempt == 0:
    print("Game over. The number was: ",number)   
    
