# PROJECT REQUIREMENTS – USER REGISTRATION SYSTEM

# * 1. DATA STORAGE
# - Create a list called registered_users for successful users
# - Create a list called failed_registrations for failed attempts

# ------------------------------------------------------------

# * 2. VALIDATION FUNCTIONS

# - validate_name(name)
# -> Name must be at least 3 characters long
# -> Return True or False

# - validate_email(email)
# -> Must contain "@" and "."
# -> Return True or False

# - validate_password(password)
# -> Must be at least 8 characters
# -> Must contain at least 1 uppercase letter
# -> Must contain at least 1 digit
# -> Return True or False

# ------------------------------------------------------------

# * 3. MAIN VALIDATION FUNCTION

# - validate_user_data(name, email, password)
# -> Calls all validation functions
# -> Raises ValueError if any validation fails
# -> Returns True if all validations pass

# ------------------------------------------------------------

# * 4. REGISTRATION FUNCTION

# - create_user_account(name, email, password)

# FUNCTION SHOULD:
# - Call validate_user_data()
# - Check if email already exists in registered_users
# - Raise ValueError if duplicate email is found
# - If valid:
#   -> Create user dictionary with name, email, password, status = "active"
#   -> Append user to registered_users
#   -> Return user dictionary

# IF ERROR OCCURS:
# - Catch ValueError
# - Store email and error message in failed_registrations
# - Return None

# ------------------------------------------------------------

# * 5. TESTING

# Test the system with:
# - Valid user
# - Duplicate email
# - Invalid name
# - Invalid email
# - Weak password

# For each test:
# - Call create_user_account()
# - Print result
# - Print registered_users
# - Print failed_registrations


# Creating 2 data storages as blank lists
registered_users = []
failed_registrations = []

# Defining the function for name,email and password validation


def validate_name(name):
    return len(name) > 3


def validate_email(email):
    return '@' in email and '.' in email


def validate_password(password):
    if len(password) < 8:
        return False

    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_uppercase and has_digit

# Main validation function that calls other functions


def validate_user_data(name, email, password):
    if not validate_name(name):
        raise ValueError("Name should be more than 3 characters")

    if not validate_email(email):
        raise ValueError("Email already exists")

    if not validate_password(password):
        raise ValueError(
            "Password should be at least 8 characters and an uppercase character")
    else:
        return True

# Function for creating users


def create_user_account(name, email, password):
    # Exception if everything is correct create user
    try:
        validate_user_data(name, email, password)

        # Check duplicate email
        for user in registered_users:
            if user['email'] == email:
                raise ValueError("Email already exist!")

        new_user = {
            "name": name,
            "email": email,
            "password": password,
            "status": "active"
        }

        # Append the current user to the data storage registered_users
        registered_users.append(new_user)
        return new_user

    except ValueError as e:  # If the validations fail throw value error
        failed_registrations.append({  # Append the email and its error to the failed_registration data storage
            "email": email,
            "error": str(e)
        })
        return None


# * =================== TESTING ========================
# Valid registration
print(create_user_account("Dren", "drenxh1@gmail.com", "Abc12345"))

# Duplicate email
print(create_user_account("John", "drenxh1@gmail.com", "Abc12345"))

# Invalid name
print(create_user_account("Al", "al@gmail.com", "Abc12345"))

# Invalid email
print(create_user_account("Mike", "mikegmail.com", "Abc12345"))

# Weak password
print(create_user_account("Sara", "sara@gmail.com", "123"))

# Final Results
print("\nREGISTERED USERS:")
print(registered_users)

print("\nFAILED REGISTRATIONS:")
print(failed_registrations)
