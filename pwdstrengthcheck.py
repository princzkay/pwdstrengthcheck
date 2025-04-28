import re

def password_strength(password):
    feedback = []
    length = len(password)
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    digits = bool(re.search(r'\d', password))
    special_char = bool(re.search(r'[^A-Za-z0-9]', password))

    score = 0

    if length >= 10:
        score += 2  # stronger weight for length
    elif length >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")
    if uppercase:
        score += 1
    else:
        feedback.append("Add uppercase letters.")
    if lowercase:
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    if digits:
        score += 1
    else:
        feedback.append("Add digits.")
    if special_char:
        score += 1
    else:
        feedback.append("Add special characters.")
    if score >= 6:
        strength = "Strong"
    elif 4 <= score < 6:
        strength = "Moderate"
    else:
        strength = "Weak"
    return strength, feedback



if __name__ == "__main__":
    pwd = input("Enter password: ")
    strength, feedback = password_strength(pwd)
    print("Password strength:", strength)
    if feedback:
        print("Suggestions to improve your password:")
        for f in feedback:
            print("-", f)


