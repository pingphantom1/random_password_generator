from models import get_user_requirements, generate_password


while True:
    print('-' * 50)
    print("Phantom's Random Password Generator")
    print('-' * 50)

    response = input("Do you want to generate a password? (yes/no): ").strip().lower()
    if response == 'no':
        print("\nOkay then, quiting...\n")
        print('-' * 50)
        break

    if response == 'yes':
        new_password = generate_password(*get_user_requirements())
        print(f"The generated password is: {new_password}")
    else:
        print("Invalid response. Enter yes or no to proceed\n")
