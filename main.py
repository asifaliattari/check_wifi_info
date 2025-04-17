import streamlit as st
import random
import string
import re

# ------------------ Blacklist ------------------
blacklist = [
    "password", "123456", "qwerty", "letmein", "admin",
    "welcome", "password123", "abc123", "111111", "iloveyou"
]

# ------------------ Strength Checker ------------------
def check_password_strength(password):
    score = 0
    feedback = []

    # Check blacklist
    if password.lower() in blacklist:
        feedback.append("This password is too common. Choose something less predictable.")
        return 1, "Weak", feedback

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Upper and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Digit
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one digit (0-9).")

    # Special character
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*).")

    # Bonus: No obvious patterns (e.g., 12345, abcd)
    if not re.search(r'(123|abc|000)', password.lower()):
        score += 1
    else:
        feedback.append("Avoid common patterns like '123', 'abc', or '000'.")

    # Determine strength label
    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Moderate"
    else:
        label = "Strong"

    return score, label, feedback

# ------------------ Password Generator ------------------
def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        _, label, _ = check_password_strength(password)
        if label == "Strong":
            return password

# ------------------ Streamlit UI ------------------
st.title("🔐 Password Strength Meter (Asif)")

st.write("Check your password strength and get tips to improve it. You can also generate a strong password.")

# Password input
user_password = st.text_input("Enter your password", type="password")

if user_password:
    score, label, feedback = check_password_strength(user_password)

    # Show strength level
    if label == "Weak":
        st.error(f"Password Strength: {label} (Score: {score}/5)")
    elif label == "Moderate":
        st.warning(f"Password Strength: {label} (Score: {score}/5)")
    else:
        st.success(f"Password Strength: {label} (Score: {score}/5)")

    # Show suggestions
    if label != "Strong":
        st.subheader("🔧 Suggestions to improve your password:")
        for tip in feedback:
            st.write(f"- {tip}")
    else:
        st.balloons()
        st.success("🎉 Your password is strong! Great job!")

# Password Generator
st.subheader("🔄 Generate a Strong Password")

if st.button("Generate Password"):
    new_password = generate_strong_password()
    st.success(f"Suggested Strong Password: `{new_password}`")
