import re
import requests
import hashlib

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

# Test the functions
password = input("Enter a password: ")
if is_complex_enough(password):
    print("Password is complex enough.")
    
    if is_password_compromised(password):
        print("Password has been compromised.")
    else:
        print("Password has not been compromised.")
else:
    print("Password is not complex enough.")
