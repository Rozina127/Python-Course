from tkinter import *

def button_clicked():
    """Function to handle button click event."""
    print("I got clicked")  # Print a message to the console
    new_text = input.get()  # Get the text from the entry widget
    my_label.config(text=new_text)  # Update the label's text with the new input

# Create the main window
window = Tk()
window.title("My First GUI Program")  # Set the title of the window
window.minsize(width=800, height=600)  # Set the minimum size of the window
window.config(padx=20, pady=20)  # Add padding around the window

# Label for the button example
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0, columnspan=2, pady=10)  # Place the label in the grid at column 0, row 0

# Button for the button example
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=0, padx=10, pady=10)  # Place the button in the grid at column 2, row 0

# Additional button for demonstration
new_button = Button(text="New Button")
new_button.grid(column=3, row=0, padx=10, pady=10)  # Place the new button in the grid at column 3, row 0

# Entry widget for text input
input = Entry(width=30)
input.grid(column=0, row=1, columnspan=4, padx=10, pady=10)  # Place the entry widget in the grid spanning columns 0 to 3

# Label, Button, and Entry widgets from the practice section

# Label
label = Label(text="This is old text")  # Create a label widget with initial text
label.config(text="This is new text")  # Update the label's text
label.grid(column=0, row=2, columnspan=4, pady=10)  # Place the label in the grid spanning columns 0 to 3

# Button
def action():
    """Function to handle the action of the button."""
    print("Do something")  # Print a message to the console

action_button = Button(text="Click Me", command=action)  # Create a button linked to the action function
action_button.grid(column=0, row=3, padx=10, pady=10)  # Place the button in the grid at column 0, row 3

# Entry widget
entry = Entry(width=30)  # Create an entry widget with a specified width
entry.insert(END, string="Some text to begin with.")  # Insert initial text into the entry
print(entry.get())  # Print the current text in the entry to the console
entry.grid(column=1, row=3, columnspan=3, padx=10, pady=10)  # Place the entry in the grid spanning columns 1 to 3

# Text widget
text = Text(height=5, width=30)  # Create a multi-line text widget with specified dimensions
text.focus()  # Set the focus to the text widget (cursor will be placed here)
text.insert(END, "Example of multi-line text entry.")  # Insert initial text into the text widget
print(text.get("1.0", END))  # Print the text in the text widget from line 1, character 0 to the end
text.grid(column=0, row=4, columnspan=4, padx=10, pady=10)  # Place the text widget in the grid spanning columns 0 to 3

# Spinbox widget
def spinbox_used():
    """Function to handle the spinbox value."""
    print(spinbox.get())  # Print the current value of the spinbox

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)  # Create a spinbox with a range from 0 to 10
spinbox.grid(column=0, row=5, padx=10, pady=10)  # Place the spinbox in the grid at column 0, row 5

# Scale widget
def scale_used(value):
    """Function to handle the scale value."""
    print(value)  # Print the current value of the scale

scale = Scale(from_=0, to=100, command=scale_used)  # Create a scale with a range from 0 to 100
scale.grid(column=1, row=5, padx=10, pady=10)  # Place the scale in the grid at column 1, row 5

# Checkbutton widget
def checkbutton_used():
    """Function to handle the checkbutton state."""
    print(checked_state.get())  # Print the value of the checked state (1 if checked, 0 if not)

checked_state = IntVar()  # Create an IntVar variable to hold the state of the checkbutton
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)  # Create a checkbutton linked to the variable
checkbutton.grid(column=2, row=5, padx=10, pady=10)  # Place the checkbutton in the grid at column 2, row 5

# Radiobutton widget
def radio_used():
    """Function to handle the radiobutton selection."""
    print(radio_state.get())  # Print the value of the selected radiobutton

radio_state = IntVar()  # Create an IntVar variable to hold the selected radio button value
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)  # Create the first radio button
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)  # Create the second radio button
radiobutton1.grid(column=0, row=6, padx=10, pady=10)  # Place the first radio button in the grid at column 0, row 6
radiobutton2.grid(column=1, row=6, padx=10, pady=10)  # Place the second radio button in the grid at column 1, row 6

# Listbox widget
def listbox_used(event):
    """Function to handle listbox selection."""
    print(listbox.get(listbox.curselection()))  # Print the currently selected item in the listbox

listbox = Listbox(height=4)  # Create a listbox with a specified height
fruits = ["Apple", "Pear", "Orange", "Banana"]  # List of items to display in the listbox
for item in fruits:
    listbox.insert(fruits.index(item), item)  # Insert each item into the listbox at the correct index
listbox.bind("<<ListboxSelect>>", listbox_used)  # Bind the listbox selection event to the listbox_used function
listbox.grid(column=2, row=6, columnspan=2, padx=10, pady=10)  # Place the listbox in the grid spanning columns 2 and 3

# Start the Tkinter event loop
window.mainloop()
