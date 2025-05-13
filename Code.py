import tkinter as tk
from tkinter import messagebox
import math
import time

# Function to calculate the brute force time estimate
def brute_force_time(guess_count):
    seconds = guess_count
    time_units = [("seconds", 1), ("minutes", 60), ("hours", 3600), ("days", 86400), ("years", 31536000)]
    
    for unit, unit_seconds in time_units:
        if seconds < unit_seconds:
            break
        seconds /= unit_seconds
        
    return f"{round(seconds, 2)} {unit}"

# Function to calculate password entropy
def calculate_entropy(password):
    char_sets = {
        "lowercase": 26,
        "uppercase": 26,
        "digits": 10,
        "special": 32  # Special characters like !@#$%^&* etc.
    }
    
    # Count the number of possible characters
    possible_characters = 0
    if any(c.islower() for c in password):
        possible_characters += char_sets["lowercase"]
    if any(c.isupper() for c in password):
        possible_characters += char_sets["uppercase"]
    if any(c.isdigit() for c in password):
        possible_characters += char_sets["digits"]
    if any(c in "!@#$%^&*()_+" for c in password):
        possible_characters += char_sets["special"]
    
    # Calculate entropy
    entropy = len(password) * math.log2(possible_characters)
    return entropy

# Function to update the UI with password statistics
def update_password_strength():
    password = password_entry.get()
    
    # Calculate password entropy
    entropy = calculate_entropy(password)
    
    # Estimate the brute force time
    guess_count = 2 ** entropy  # Estimate the guesses needed for brute-forcing
    time_estimate = brute_force_time(guess_count)
    
    # Update entropy and time estimate
    entropy_label.config(text=f"Entropy: {round(entropy, 2)} bits")
    time_label.config(text=f"Brute Force Time: {time_estimate}")
    
    # Provide password tips
    tips = []
    if len(password) < 8:
        tips.append("Make your password longer.")
    if not any(char.isdigit() for char in password):
        tips.append("Include numbers.")
    if not any(char.islower() for char in password):
        tips.append("Include lowercase letters.")
    if not any(char.isupper() for char in password):
        tips.append("Include uppercase letters.")
    if not any(char in "!@#$%^&*()_+" for char in password):
        tips.append("Add special characters.")
    
    # Update tips in the UI
    if tips:
        tips_label.config(text="Tips: " + "\n".join(tips))
    else:
        tips_label.config(text="Tips: Strong password!")
    
    # Update the background color based on the password strength
    if entropy > 40:
        root.config(bg="lightgreen")
        status_label.config(text="Good Password", fg="green")
    elif 20 < entropy <= 40:
        root.config(bg="lightyellow")
        status_label.config(text="Bad Password", fg="orange")
    else:
        root.config(bg="lightcoral")
        status_label.config(text="Worst Password", fg="red")

# Setting up the GUI
root = tk.Tk()
root.title("Password Strength Visualizer")

# Adjust window size
root.geometry("400x400")

# Password Entry
password_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
password_entry.pack(pady=10)

# Button to analyze password strength
check_button = tk.Button(root, text="Check Strength", command=update_password_strength, font=("Arial", 12))
check_button.pack(pady=20)

# Labels to display results
entropy_label = tk.Label(root, text="Entropy: 0 bits", font=("Arial", 12))
entropy_label.pack(pady=5)

time_label = tk.Label(root, text="Brute Force Time: 0 seconds", font=("Arial", 12))
time_label.pack(pady=5)

status_label = tk.Label(root, text="Password Strength", font=("Arial", 14, "bold"))
status_label.pack(pady=10)

tips_label = tk.Label(root, text="Tips: ", font=("Arial", 12))
tips_label.pack(pady=10)

# Run the application
root.mainloop()
