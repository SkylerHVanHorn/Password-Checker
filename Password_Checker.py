import re
import requests
import hashlib
import secrets
import string

def is_complex_enough(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

def is_password_compromised(password):
    # Hash the password using SHA-1
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = hashed_password[:5], hashed_password[5:]
    
    # Make a request to the Have I Been Pwned API
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)
    
    # Check if the suffix of the hash appears in the response
    return suffix in response.text

def generate_secure_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(alphabet) for _ in range(12))  # Generate a 12-character password
    return secure_password

# Main
password = input ("Welcome to my NIST password checker. Please enter a password or q to quit: ")
while (password != 'q'):
    if not is_password_compromised(password) and password != 'q':
        print("The entered password has been compromised and should be replaced")
        print("Generating a new secure password...")
        new_password = generate_secure_password()
        print("New secure password:", new_password)
    else:
        if not is_complex_enough(password) and password != 'q':
            print("The entered password is not complex enough and should be replaced")
            print("Generating a new secure password...")
            new_password = generate_secure_password()
            print("New secure password:", new_password)
        else:
            print("Password is complex enough and has not been compromised.")
    password = input("Enter a password or q to quit: ")
