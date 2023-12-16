import random

def roll_dice(number_of_dice):
    return [random.randint(1, 6) for _ in range(number_of_dice)]

def main():
    try:
        num_dice = int(input("Enter the number of dice to roll: "))
        if num_dice <= 0:
            raise ValueError("Number of dice must be a positive integer.")
        
        print(f"Rolling {num_dice} dice...")
        results = roll_dice(num_dice)
        print("Results:", results)
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nDice rolling aborted by user.")

if __name__ == "__main__":
    main()

