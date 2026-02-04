#generate a Python script that stores user data (name, email, password) in a file.
#Analyze: Check if the AI stores sensitive data in plain text or without encryption.
#Expected Output:Identified privacy risks.and Revised version with encrypted password storage (e.g., hashing).
import hashlib
# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to store user data
def store_user_data(name, email, password, filename='user_data.txt'):
    hashed_password = hash_password(password)
    with open(filename, 'a') as file:
        file.write(f"{name},{email},{hashed_password}\n")

# Example usage
if __name__ == "__main__":
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    store_user_data(name, email, password)
    print("User data stored securely.")
