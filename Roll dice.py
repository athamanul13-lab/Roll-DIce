import random

def roll_dice():
   
    print("          ROLL DICE          ")

    
    while True:
        user_input = input("\nHow many dice do you want to roll? (or type 'quit' to exit): ").strip().lower()
        
        if user_input == "quit":
            print("\nThanks for rolling! Goodbye")
            break
            
        try:
            num_dice = int(user_input)
            if num_dice <= 0:
                print("Please enter a number greater than 0!")
                continue
                
           
            results = [random.randint(1, 6) for _ in range(num_dice)]
            total_sum = sum(results)
            
            print("\n------------------------------------------")
            print(f"Dice Results: \033[1;33m{results}\033[0m")
            print(f"Total Sum   : \033[1;32m{total_sum}\033[0m")
            print("------------------------------------------")
            
        except ValueError:
            print("Invalid input! Please enter a valid number or 'quit'.")

if __name__ == "__main__":
    roll_dice()