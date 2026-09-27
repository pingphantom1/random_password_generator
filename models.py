import string
import secrets


def get_user_requirements():
    print("Answer the following questions with 'Yes' or 'NO'to determine what your password should contain")
    include_upper_case = input("Include uppercase letters?:  ").strip().lower()
    include_lower_case  = input("Include lowercase letters?: ").strip().lower()
    include_digits = input("Include digits?: ").strip().lower()
    include_special_characters = input("Include special symbols/punctuation (!@#$%^&*...)?: ").strip().lower()
    

    passwd_requirements = [include_upper_case, include_lower_case, include_digits, include_special_characters]

    def get_passwd_length(): # Geet user to input the desired password length
        while True: #Loop this function when user enters a value that is not a number
            try:
                get_required_passwd_length = input("\nEnter the preferred length of the password: ").strip() # Remove beginning or trailing spaces from user input
                preferred_length = int(get_required_passwd_length)
                return preferred_length
            except ValueError:
                print("Invalid input, please enter a valid number (eg. 12, 16)")
            except Exception as e:
                print(f"An unexpected error occured. Error: {e}")

    passwd_length = get_passwd_length()
    passwd_requirements.append(passwd_length)
        
    return passwd_requirements


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
        char_set for (_, char_set), passwd_requirements in zip(categories, passwd_requirements[:-1])
        if passwd_requirements == "yes"
    )

    if not character_pool:
        return "Error: Select at least one character type."

    password = "".join(
        secrets.choice(character_pool)
        for _ in range(passwd_length)
        )

    return password