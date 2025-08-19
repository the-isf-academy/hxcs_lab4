# /////////// INSTRUCTIONS /////////////////
# 🎲 Let's make a simple timer, we can incorporate this into any game!

# 💻️⃣ Run the file multiple times to test the timer
#    - Currently, it does not display an accurate total_time 

# 💻️⃣ In line 21, fix the total_time

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

from time import time 

start_time = time()

user_name = input("Enter your name: ")

print(f"Hello {user_name}!")

end_time = time()

total_time = 0

print(f"It took you {total_time}s to enter your name.")


