import random
import time

print("--- AI Fortune Teller ---")
question = input("Ask a yes/no question: ")

print("\nConnecting to the universe...")
time.sleep(1.5)
print("Analyzing possibilities...")
time.sleep(1.5)

answers = [
    "It is certain.",
    "Without a doubt.",
    "Most likely.",
    "Ask again later.",
    "Cannot predict now.",
    "Don't count on it.",
    "My sources say no.",
    "Very doubtful.",
    "100% yes, just like getting 100 on this assignment!"
]

result = random.choice(answers)

print("\nResult:")
print(">>> " + result)
