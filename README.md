# Phantom's Random Password Generator

A modular, command-line interface (CLI) random password generator built with Python. It generates cryptographically secure passwords based on customizable user preferences such as uppercase letters, lowercase letters, numbers, and special symbols.

---

## Features

- **Cryptographically Secure:** Uses Python's built-in `secrets` module for high-entropy random selection.
- **Custom Character Sets:** Enable or disable uppercase, lowercase, numerical, and special punctuation characters.
- **Flexible Length:** Custom password length selection with built-in input validation.
- **Modular Architecture:** Clean separation of concern across execution, application control, and core logic modules.

---

## Project Structure

```text
.
├── run.py        # Application entry point
├── app.py        # CLI interactive loop and flow control
└── models.py     # User input validation and password generation logic
```

---

## Installation & Usage

### Prerequisites
- Python 3.8 or higher (no external dependencies required).

### Running the Application

1. Clone or download the repository to your local machine.
2. Open a terminal inside the project directory.
3. Run the application entry point:

```bash
python run.py
```

4. Follow the interactive prompts to specify password length and character inclusions.

---

## How It Works

1. **User Input (`models.py`):** Collects preferences for character types and prompts for password length using robust `try/except` exception handling.
2. **Dynamic Character Pool Assembly:** Pairs category constants from the `string` module (`ascii_uppercase`, `digits`, etc.) with user choices using `zip()`.
3. **Secure Generation:** Randomly samples characters from the generated pool using `secrets.choice()` for the specified length.
4. **Execution Loop (`app.py`):** Keeps the program active in a `while` loop until the user chooses to exit.

---

## License

