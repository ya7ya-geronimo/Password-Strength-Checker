import re
import math
import tkinter as tk
from tkinter import ttk

# Common weak passwords (sample)
COMMON_PASSWORDS = {
    "password", "123456", "qwerty", "admin",
    "letmein", "welcome", "iloveyou"
}

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)

def check_password(event=None):
    password = entry.get()
    feedback = []
    score = 0

    if not password:
        update_ui(0, "Very Weak", "Enter a password")
        return

    if password.lower() in COMMON_PASSWORDS:
        update_ui(10, "Very Weak", "Common password detected ❌")
        return

    entropy = calculate_entropy(password)

    # Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        feedback.append("Use at least 8 characters")

    # Complexity checks
    if re.search(r"[A-Z]", password): score += 15
    else: feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password): score += 15
    else: feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password): score += 15
    else: feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        feedback.append("Add special characters")

    # Entropy bonus
    if entropy > 60:
        score += 15

    score = min(score, 100)

    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    else:
        strength = "Strong"

    update_ui(score, strength, " | ".join(feedback) if feedback else "Great password 👍")

def update_ui(score, strength, message):
    result_label.config(text=f"Strength: {strength} | Score: {score}/100")
    feedback_label.config(text=message)
    progress["value"] = score

    if score < 40:
        progress.configure(style="Red.Horizontal.TProgressbar")
    elif score < 70:
        progress.configure(style="Yellow.Horizontal.TProgressbar")
    else:
        progress.configure(style="Green.Horizontal.TProgressbar")

# GUI
root = tk.Tk()
root.title("Advanced Password Strength Checker")
root.geometry("420x280")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 11)).pack(pady=10)

entry = tk.Entry(root, show="*", width=32, font=("Arial", 11))
entry.pack()
entry.bind("<KeyRelease>", check_password)

progress = ttk.Progressbar(root, length=300, maximum=100)
progress.pack(pady=15)

result_label = tk.Label(root, text="Strength: ", font=("Arial", 11, "bold"))
result_label.pack()

feedback_label = tk.Label(root, text="", wraplength=380, fg="gray")
feedback_label.pack(pady=10)

# Progress bar styles
style = ttk.Style()
style.theme_use("default")
style.configure("Red.Horizontal.TProgressbar", background="red")
style.configure("Yellow.Horizontal.TProgressbar", background="orange")
style.configure("Green.Horizontal.TProgressbar", background="green")

root.mainloop() 