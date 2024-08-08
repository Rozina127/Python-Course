from tkinter import *  # Import tkinter for GUI components
from tkinter import messagebox  # Import messagebox for displaying pop-up messages
from random import choice, randint, shuffle  # Import functions to generate random passwords
import pyperclip  # Import pyperclip to copy generated passwords to the clipboard
import json  # Import json to handle saving and loading of password data

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Function to generate a random password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random letters, symbols, and numbers for the password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine and shuffle the characters
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Join the characters into a single string and insert into the password entry field
    password = "".join(password_list)
    password_entry.insert(0, password)

    # Copy the generated password to the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Function to save the entered website, email, and password to a file
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Create a dictionary to store the new data
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check if any fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Try to open the existing data file
            with open("day29projectdata.json", "r") as data_file:
                # Load the old data
                data = json.load(data_file)
        except FileNotFoundError:
            # If the file does not exist, create a new one with the new data
            data = new_data  # Start with the new data if the file doesn't exist
        else:
            # Update the old data with the new data
            data.update(new_data)

        # Save the updated data back to the file (or create a new file if it didn't exist)
        with open("day29projectdata.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        # Clear the website and password entry fields
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

# Function to find and display the password for a given website
def find_password():
    website = website_entry.get()

    try:
        # Try to open the data file
        with open("day29projectdata.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        # If the file does not exist, show an error message
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            # If the website exists in the data, retrieve the email and password
            email = data[website]["email"]
            password = data[website]["password"]
            # Display the email and password in a message box
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            # If the website does not exist, show an error message
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #

# Create the main window
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)  # Increase padding to make the window larger

# Create a canvas for the logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="day29projectlogo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels for website, email, and password
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=5)  # Add padding between the rows
email_label = Label(text="Email:")
email_label.grid(row=2, column=0, pady=5)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=5)

# Entry fields for user input
website_entry = Entry(width=25)  # Reduced width to align better with buttons
website_entry.grid(row=1, column=1, pady=5)
website_entry.focus()  # Set focus on the website entry field
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "RozinaWaliKhan123@gmail.com")  # Pre-fill the email entry field
password_entry = Entry(width=25)  # Reduced width to align better with buttons
password_entry.grid(row=3, column=1, pady=5)

# Buttons for search, password generation, and saving
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2, pady=5)  # Add padding between buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, pady=5)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

# Start the Tkinter event loop
window.mainloop()
