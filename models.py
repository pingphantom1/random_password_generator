import string
import secrets


def get_user_requirements():
    print("Answer the following questions with 'Yes' or 'NO'to determine what your password should contain")
    include_upper_case = input("Include uppercase letters?:  ").strip().lower()
    include_lower_case  = input("Include lowercase letters?: ").strip().lower()
    include_digits = input("Include digits?: ").strip().lower()
    include_special_characters = input("Include special symbols/punctuation (!@#$%^&*...)?: ").strip().lower()
    

    requirements = [include_upper_case, include_lower_case, include_digits, include_special_characters]
    return requirements

def get_passwd_length(uppercase, lowercase, digits, punctuation): # Geet user to input the desired password length
    passwd_requirements = [uppercase, lowercase, digits, punctuation]
    
    while True: #Loop this function when user enters a value that is not a number
        try:
            get_required_passwd_length = input("\nEnter the preferred length of the password: ").strip() # Remove beginning or trailing spaces from user input
            preferred_length = int(get_required_passwd_length)

            # prevent negative or zero password length
            if preferred_length <= 0 or preferred_length == 0 or type(preferred_length) == str:
                print("Invalid length. Password length cannot be 0 or a negative number or text")
                preferred_length = get_passwd_length()
            else:
                passwd_requirements.append(preferred_length)
                
            return passwd_requirements
        except ValueError:
            print("Invalid input, please enter a valid number (eg. 12, 16)")
        except TypeError:
            print("Invalid input, please enter a valid positive number (eg. 12, 16)")
        except Exception as e:
            print(f"An unexpected error occured. Error: {e}")


def generate_password(*args):
     # args unpacks to: (uppercase, lowercase, digits, punctuation, length)
    passwd_requirements = list(args)
    passwd_length = passwd_requirements[-1] # pick the passwd length the first index from the end of the list

    # Map each preference in order to its character set
    categories = [
        ("uppercase", string.ascii_uppercase),
        ("lowercase", string.ascii_lowercase),
        ("digits", string.digits),
        ("punctuation", string.punctuation),
    ]

    # Build the pool: only add a set if the user said "yes"
    character_pool = "".join(
        char_set for (_, char_set), passwd_pref in zip(categories, passwd_requirements[:-1])
        if passwd_pref == "yes"
    )

    if not character_pool:
        return "Error: Select at least one character type."
    while True:
        try:
            password = "".join(
                secrets.choice(character_pool)
                for _ in range(passwd_length)
                )
            return password
        except TypeError:
            print("Invalid length. Password length cannot be 0 or a negative number")
            passwd_length = get_passwd_length()