import random
import string

def generate_password(length):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    characters = lowercase + uppercase + digits + symbols

    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    
    password = generate_password(length)
    
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
