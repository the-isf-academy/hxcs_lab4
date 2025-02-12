# /////////// INSTRUCTIONS /////////////////
# 🎲  Let's make a simple number guessing game 

# 🔁  We will use a for loop to allow the user to guess multiple times

# 💻️⃣  Run the file multiple times to play test the game 

# 💻️⃣  Change the for loop so the user can guess 5 times

# 💻️⃣  If the user does not win, print a losing statement

# 💻  Add an elif statement to tell the user if their guess was too low 

# ------------------
# 🧐 Extension
#    1) before the game beginings, allow the user to choose easy, medium, hard mode 
#       - this will change the random number range 
#
#    2) Add in a timer, the user has 5 seconds to answer each question (look at file_ex_timer.py)
# --------------------
# For an extra challenge, delete all of the code below, and code the game from scratch :)
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

