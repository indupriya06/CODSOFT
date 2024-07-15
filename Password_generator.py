import re
import secrets
import string
user_input = int(input("Enter the desired length of the password:"))
def generate_password(length=user_input,nums=1,special_chars=1,uppercase=1,lowercase=1):
    "This function accepts a parameter 'len' and returns a randomly generated password"
    #Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    #combine all characters
    all_characters = letters+digits+symbols
    while True:
        password = ''
        #Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        constraints = [
            (nums, r'\d'), (special_chars,fr'[{symbols}]'), (uppercase, r'[A-Z]'), (lowercase, r'[a-z]')
            ]
        #check constraints
        if all(
            constraint <= len(re.findall(pattern,password))
            for constraint,pattern in constraints
        ):
            break
    return password
if __name__ == '__main__':
    new_password = generate_password()
    print(new_password)
            
