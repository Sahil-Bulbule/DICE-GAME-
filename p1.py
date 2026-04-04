import random

def roll_dice():
    return random.randint(1, 6)  # Dice has 6 sides

def main():
    print("🎲 Welcome to the Dice Roller Simulator! 🎲")
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result}!\n")
        
        choice = input("Do you want to roll again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
    