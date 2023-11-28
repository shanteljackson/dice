import random

def roll_die():
    return random.randint(1, 6)

# Rolling a single die
print("Rolling a die...")
result = roll_die()
print(f"Result: {result}")

