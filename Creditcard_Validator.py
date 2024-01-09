import tkinter as tk
import re

def validate_credit_card():
    card_number = entry.get()  # Get the input from the entry field
    card_number = re.sub(r'\D', '', card_number)  # Remove non-numeric characters

    if not card_number.isdigit():
        result_label.config(text="Invalid Input! Only digits allowed.")
        return

    # Apply Luhn algorithm to validate the card number
    total = 0
    is_second = False
    for digit in card_number[::-1]:
        digit = int(digit)
        if is_second:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        is_second = not is_second

    if total % 10 == 0:
        card_type = detect_card_type(card_number)
        result_label.config(text=f"Valid {card_type} card number")
    else:
        result_label.config(text="Invalid credit card number")

def detect_card_type(card_number):
    # Define patterns for different card types
    patterns = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$"
    }

    for card_type, pattern in patterns.items():
        if re.match(pattern, card_number):
            return card_type

    return "Unknown"

# Create a tkinter window
root = tk.Tk()
root.title("Credit Card Validator")
root.configure(bg="skyblue")

header_label = tk.Label(root, text="CREDITCARD VALIDATOR", fg="red", bg="skyblue", font=("Arial", 16))
header_label.pack()

# Create and place widgets
label = tk.Label(root, text="Enter credit card number:", fg="blue", bg="lime", font=("Arial", 14))
label.pack()

entry = tk.Entry(root,font=("Arial", 14))
entry.pack()

validate_button = tk.Button(root, text="Validate", command=validate_credit_card, fg="blue", bg="yellow", font=("Arial", 14))
validate_button.pack()

result_label = tk.Label(root, text="",bg="skyblue",fg="red",font=("Arial", 13))
result_label.pack()

# Start the tkinter main loop
root.mainloop()
