def check_password_strength(password):
    # Set the strength score to start at 0.
    strength = 0

    # Check length (at least 10 characters).
    if len(password) < 10:
        return "Weak password. You must add at least {} more characters.".format(10 - len(password))

    strength += 1  # Length is sufficient.

    # Check if the password contains uppercase letters.
    if not any(char.isupper() for char in password):
        return "Weak password. You must include capital letters."

    strength += 1  # Contains uppercase.

    # Check if the password contains lowercase letters.
    if not any(char.islower() for char in password):
        return "Weak password. You need to add lowercase letters."

    strength += 1  # Contains lowercase.

    # Check if the password contains digits.
    if not any(char.isdigit() for char in password):
        return "Weak password. You need to add digits."

    strength += 1  # Contains digits.

    # Check if the password contains special characters.
    special_chars = "!@#$%^&*()_+[]}{|;:,.<>?~"
    if not any(char in special_chars for char in password):
        return "Weak password. You need to add special characters."

    strength += 1  # Contains special characters.

    # Check if the password contains repeating characters.
    if any(password[i] == password[i + 1] == password[i + 2] for i in range(len(password) - 2)):
        return "Weak password. Avoid using the same character more than twice in a row."

    strength += 1  # No repeating characters

    # Check if the password contains consecutive letters or digits
    for i in range(len(password) - 2):
        if password[i].isalpha() and password[i + 1].isalpha() and password[i + 2].isalpha():
            if abs(ord(password[i]) - ord(password[i + 1])) == 1 and abs(ord(password[i + 1]) - ord(password[i + 2])) == 1:
                return "Weak password. Avoid using more than 2 consecutive letters."
        elif password[i].isdigit() and password[i + 1].isdigit() and password[i + 2].isdigit():
            if abs(int(password[i]) - int(password[i + 1])) == 1 and abs(int(password[i + 1]) - int(password[i + 2])) == 1:
                return "Weak password. Avoid using more than 2 consecutive digits."

    strength += 1  # No consecutive letters or digits

    # If all conditions are met, the password is strong
    return "Strong password!" if strength == 7 else "Weak password. Please choose a stronger one."

while True:
    user_password = input("Enter a password: ")
    strength_score = check_password_strength(user_password)
    print(strength_score)
    if strength_score == "Strong password!":
        break
    else:
        print("Please try again.")
