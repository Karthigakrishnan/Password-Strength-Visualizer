# 🔐 Password Strength Visualizer 💥

Welcome to the **Password Strength Visualizer**, the quirky little app that tells your password the **brutal truth** — is it 💪 strong, 😬 meh, or 💀 absolutely terrible?

## 🎯 What is this?

This is a colorful, interactive, and easy-to-use **Python Tkinter GUI application** that:

- Calculates your password's **entropy** (a fancy way of saying “how unpredictable is this?”).
- Estimates the **time it would take a brute-force attack** to crack your password.
- Gives you honest and sometimes sassy **feedback** on how to improve your password.
- Changes background colors to visually represent the strength:
  - 🟢 **Good**: Nice job, hacker-proof legend!
  - 🟡 **Bad**: Not terrible, but could be stronger.
  - 🔴 **Worst**: Might as well be `password123`.

---

## 📦 Features

- ✅ Real-time password entropy analysis
- ✅ Brute-force crack time estimation (in seconds, minutes, hours, etc.)
- ✅ Color-coded feedback for instant clarity
- ✅ Tips to improve your password game
- ✅ Clean, simple, and beginner-friendly GUI built with Tkinter

---

## 🎮 How to Use

1. **Clone this repo** (or just copy the Python file):
   ```bash
   git clone https://github.com/yourusername/password-strength-visualizer.git
   cd password-strength-visualizer
   
2.Run the script:
  python password_visualizer.py
  
3.Type in a password, hit "Check Strength", and enjoy the judgment!

🎨 Password Strength Criteria
        
        | Entropy (bits)	| Strength  |	Background Color	| Message           |
        | > 40	          | Good 💪  	| Light Green	      | "Good Password!"  |
        | 20 - 40         |	Bad 😬	  | Light Yellow	    | "Bad Password!"   |
        | < 20	          | Worst 💀	| Light Coral	      | "Worst Password!" |
