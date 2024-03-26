# Name: Case Buckmaster
# Lab: 4.15
# Description: Takes a password and alters certain values to strengthen the password.

# Variables

# Used to obtain the password input.
original_password = input()

# Used to later store the improved password.
new_password = ""

# Check for any key characters in the string to alter. Otherwise, keep the character the same.
for character in original_password:
    if character == "i":
        new_password += "!"

    elif character == "a":
        new_password += "@"

    elif character == "m":
        new_password += "M"

    elif character == "B":
        new_password += "8"

    elif character == "o":
        new_password += "."

    else:
        new_password += character

# Add a few additional characters to the string for extra security.
new_password += "q*s"

# Display the new password.
print(new_password)
