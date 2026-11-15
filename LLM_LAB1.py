#Nelson Davis
#November 11th  
#LLM_LAB1
#A Random password generator

import string
import secrets

def generate_passwords(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    #Build the pool of characters based on user preferences
    alphabet = ""
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_lower:
        alphabet += string.ascii_lowercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation

    if not alphabet:
        raise ValueError("At least one character type must be selected. ") 

    # Generate the secure random password
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Example usage:G
if __name__ == "__main__":
    # Generate a 16-character password with letters, numbers, and symbols
    my_password = generate_passwords(length=16)
    print(f"Generated Password: {my_password}")

    