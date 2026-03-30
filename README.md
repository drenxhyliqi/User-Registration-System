USER REGISTRATION SYSTEM

This project is a simple user registration system built using core Python concepts such as functions, lists, dictionaries, loops, and exception handling.

The system simulates how a basic backend registration process works.

WHAT THE SYSTEM DOES:

- Takes user input (name, email, password)
- Validates all user data using custom validation functions
- Checks if the email already exists in the system
- Creates a user account if everything is valid
- Stores successful users in a list called registered_users
- Stores failed registration attempts in failed_registrations
- Handles errors using exception handling (ValueError)
- Returns the created user or None if registration fails

SYSTEM BEHAVIOR:

1. If registration is successful:
   - A user dictionary is created
   - User is added to registered_users
   - The user object is returned

2. If registration fails:
   - The error is caught
   - The failure is logged in failed_registrations
   - The function returns None

PURPOSE:

This project helps simulate real-world registration logic and improves understanding of:
- Validation logic
- Error handling
- Functions and modular code
- Data structures (lists & dictionaries)