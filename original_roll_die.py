import random

def roll_dice(number_of_dice):
    return [random.randint(1, 6) for _ in range(number_of_dice)]

# User inputs the number of dice to roll
num_dice = int(input("Enter the number of dice to roll: "))

# Rolling the dice
print(f"Rolling {num_dice} dice...")
results = roll_dice(num_dice)
print("Results:", results)

