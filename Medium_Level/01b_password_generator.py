"""
Create a password of length N from a string which consists of all alphabets, numbers and special characters. Once the password is created, check if it has a number and / or special character depending on the conditions.
This method ensures that there can be multiple numbers and special characters in our password.
"""

import random
import string

# Global strings to be used to randomly generate password components
string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_num = '0123456789'
string_special = '~!@#$%^&*()'

def userInput():
    length = int(input("Enter the length of the password: "))
    use_special_chars = input("Include special characters?(yes/no):").lower() == 'yes'
    use_numbers = input("Include numbers?(yes/no): ").lower() == 'yes'
    return(length, use_special_chars, use_numbers)

def generate_password(length, use_special_chars, use_numbers):
    """Generates a random password based on user preferences."""
    password = ''

    if use_numbers and use_special_chars:
        for i in range(length):
            password = password + random.choice(string_num+string_char+string_special)
    elif use_numbers and not use_special_chars:
        for i in range(length):
            password = password + random.choice(string_num+string_char)
    elif not use_numbers and use_special_chars:
        for i in range(length):
            password = password + random.choice(string_char+string_special)
    else:
        for i in range(length):
            password = password + random.choice(string_char)

    return password


if __name__ == '__main__':
    length, use_special_chars, use_numbers = userInput()
    generated_password = generate_password(length, use_special_chars, use_numbers)
    print("\nGenerated Password: \n", generated_password)