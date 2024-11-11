import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

# Main function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game!")
        print("Choose 'rock', 'paper', or 'scissors' to play.")
        
        # Get user input
        user_choice = input("Your choice: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Get computer's choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        # Display current score
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nFinal Score:")
    print(f"You: {user_score}, Computer: {computer_score}")
    print("Thanks for playing!")

# Run the game
play_game()
