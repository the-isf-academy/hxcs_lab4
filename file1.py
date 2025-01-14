# /////////// INSTRUCTIONS /////////////////
# 🎲 Let's make a simple number guessing game 

# 🔁 We will use a for loop to allow the user to guess multiple times

# 💻️⃣ Run the file multiple times to play test the game 

# 💻️⃣ Change the for loop so the user can guess 5 times

# 💻️⃣ Customize the print statement if the user does not win (line 50)

# 💻 Add an elif statement to tell the user if their guess was too low (line 42)

# ------------------
# 🧐 Extension
#     1) Print a different final message depending on if the user guessed correctly or incorrectly
#     2) allow the user to choose a easy, medium, hard mode 
#          - this will change the random number range 
# ////////////////////////////////////////////

from random import randint 

print("--- 🎲 Welcome to the Number Guessing Game 🎲 ---\n")

# stores random integer in a variable (experiment with changing these numbers)
random_number = randint(1,10)      

for i in range(2): 

  user_guess = int(input("Guess a number bewtween 1-10: "))

  if user_guess == random_number: 
    print(f"👏 Correct!\n")

    # leave the loop if user guesses correctly 
    break    

  elif user_guess > random_number:
    print(f" ...too high\n")  

  # ⬇️ your elif statement goes below here 


  
print("-"*20)

if user_guess == random_number:
    print(f"👋 Thanks for playing!")
else:
    print(f"👋 Thanks for playing!")

