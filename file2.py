# /////////// INSTRUCTIONS /////////////////
# 🎲 Let's make a simple math guessing game

# 💻️⃣ Run the file multiple times to play test the game 

# 💻️⃣ Currently, it always adds a number to 10. 
#       Make the game more difficult by making num1 and num2 random 

# 💻 Using if, elif and print statements - tell the user if they guessed correctly or incorrectly
#       (line 36)

# 💻 Fix the score
#       - if the user gueses correctly
#       - and if the user guessed in less than 3 seconds
#       - the scores increase by 1

# ////////////////////////////////////////////

import random
import time

score = 0

for i in range(5):
    num1 = random.randint(1, 10)
    num2 = 10
    answer = num1 + num2
    
    print(f"What is {num1} + {num2}")    

    start_time = time.time()
    user_answer = int(input("--- Your answer: "))
    end_time = time.time()
    
    total_time_seconds = round(end_time - start_time,3)
    
    # ⬇️ tell the user if they were correct and incorrect 
    
    print(f"(It took you {total_time_seconds} seconds)")
        
    score += 1
    print()
   
print(f"Quiz completed. Your score: {score}")


