import random 
import string


#Derive all the characters, letters and digits that can be used for the password
def generated_password(upper, lower, char, digit):
    uppercase = string.ascii_uppercase
    Upper = random.choices(uppercase, k=upper)

    lowercase = string.ascii_lowercase
    Lower = random.choices(lowercase, k=lower)
    
    blocked_chars = ['"', "'", "//", " ", "|", "`", "~", "<", ">", ".", ",", '/']
    special_characters = ''.join(c for c in string.punctuation if c not in blocked_chars )
    Characters = random.choices(special_characters, k=char)
    
    numbers = string.digits
    Digits = random.choices(numbers, k=digit)

    #join the combo based on the number of each the user requests for
    password = Upper + Lower + Characters + Digits  
    
    #It then shuffles the password so it doesn't have a specific pattern to improve security 
    random.shuffle(password)
    
    return "" .join(password)

def main():
    #Prompts the user for number of Uppercase, lowercase, characters and digits respectively 
    aocl = int(input("How many capital letters: "))
    aosl = int(input("How many small letters: "))
    aoc = int(input("How many special characters: "))
    aon = int(input("How many numbers: "))


    Password = generated_password(aocl, aosl, aoc, aon)
    print(f"Your passowrd: {Password}")


main()