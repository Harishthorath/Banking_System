import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔑 Password Generator")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        if length < 4:
            print("Password length should be at least 4 characters.")
            return
        password = generate_password(length)
        print(f"Your secure password is: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
