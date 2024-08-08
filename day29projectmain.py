from tkinter import *  # Import all classes and functions from tkinter for GUI
from tkinter import messagebox  # Import messagebox for displaying pop-up messages
from random import choice, randint, shuffle  # Import functions to help generate random passwords
import pyperclip  # Import pyperclip to copy the generated password to clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Function to generate a random password
def generate_password():
    # Lists of characters to use in the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly choose letters, symbols, and numbers for the password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]  # 8-10 random letters
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]  # 2-4 random symbols
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]  # 2-4 random numbers

    # Combine all the characters
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)  # Shuffle the combined list to make the password more secure

    # Join the characters into a single string
    password = "".join(password_list)
    password_entry.insert(0, password)  # Insert the generated password into the password entry field
    pyperclip.copy(password)  # Copy the generated password to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Function to save the entered website, email, and password to a file
def save():

    # Get the entered website, email, and password
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if any fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")  # Show an error if fields are empty
    else:
        # Ask the user for confirmation before saving
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:  # If the user confirms
            # Save the details to a file named "data.txt"
            with open("day29projectdata.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")  # Write the details in the file
                website_entry.delete(0, END)  # Clear the website entry field
                password_entry.delete(0, END)  # Clear the password entry field


# ---------------------------- UI SETUP ------------------------------- #

# Create the main window
window = Tk()
window.title("Password Manager")  # Set the window title
window.config(padx=100, pady=100)  # Add padding around the window

# Create a canvas for the logo
canvas = Canvas(height=200, width=200)  # Create a canvas of size 200x200 pixels
logo_img = PhotoImage(file="logo.png")  # Load the logo image
canvas.create_image(100, 100, image=logo_img)  # Place the logo image at the center of the canvas
canvas.grid(row=0, column=1)  # Position the canvas in the grid

# Labels for website, email/username, and password fields
website_label = Label(text="Website:")  # Label for the website field
website_label.grid(row=1, column=0)  # Position the website label in the grid
email_label = Label(text="Email/Username:")  # Label for the email/username field
email_label.grid(row=2, column=0)  # Position the email label in the grid
password_label = Label(text="Password:")  # Label for the password field
password_label.grid(row=3, column=0)  # Position the password label in the grid

# Entry fields for user input
website_entry = Entry(width=35)  # Entry field for the website
website_entry.grid(row=1, column=1, columnspan=2)  # Position the website entry field in the grid
website_entry.focus()  # Focus on the website entry field when the window opens
email_entry = Entry(width=35)  # Entry field for the email/username
email_entry.grid(row=2, column=1, columnspan=2)  # Position the email entry field in the grid
email_entry.insert(0, "rozinawalikhan123@gmail.com")  # Pre-fill the email entry field with a default email
password_entry = Entry(width=21)  # Entry field for the password
password_entry.grid(row=3, column=1)  # Position the password entry field in the grid

# Buttons for generating password and saving the information
generate_password_button = Button(text="Generate Password", command=generate_password)  # Button to generate password
generate_password_button.grid(row=3, column=2)  # Position the generate password button in the grid
add_button = Button(text="Add", width=36, command=save)  # Button to add/save the password information
add_button.grid(row=4, column=1, columnspan=2)  # Position the add button in the grid

# Start the Tkinter event loop
window.mainloop()
