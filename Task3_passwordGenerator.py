import random
import string

# Function to generate a password
def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
try:
    length = int(input("Enter the desired password length: "))
    if length < 1:
        print("Please enter a length greater than 0.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a valid number for length.")
