# /////////// INSTRUCTIONS /////////////////
# 🎲 Let's make a simple number guessing game 

# 🔁 We will use a for loop to allow the user to guess multiple times

# 💻️⃣ Run the file multiple times to play test the game 

# 💻️⃣ Add 3 more questions, play test the game with the new questions

# 💻 Add an if statement to tell the user if they were correct

# 💻 Add an else statement to tell the user if they were incorrect 

# 💻 Increase the score when the user guesses correctly

# 💻 Add in a timer, the user has 5 seconds to answer each question

# ------------------
# 🧐 Extension
#     1) Randomize the order of the questions
#     2) allow the user to choose a easy, medium, hard mode 
#          - this will change the random number range 
# ////////////////////////////////////////////

questions_data = {
    "What is the capital of France?": "Paris",
    "Who wrote Romeo and Juliet?": "William Shakespeare",
    "What is the largest mammal in the world?": "Blue Whale",
}

score = 0
for question, answer in questions_data.items():

    print(f"❓ {question}")

    user_guess = input("--- Enter a guess: ")
    
    # ⬇️ your if statement goes here  
    
    
    # ⬇️ your else statement goes here  

    print()

print(f"Your score: {score}")
