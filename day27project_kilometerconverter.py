from tkinter import *

# Function to convert miles to kilometers
def convert_miles_to_kilometers():
    try:
        miles = float(miles_entry.get())  # Get the miles input from the entry widget
        kilometers = miles * 1.60934  # Convert miles to kilometers
        result_label.config(text=f"{miles} miles is equal to {kilometers:.2f} kilometers")  # Update the result label with the conversion
    except ValueError:
        result_label.config(text="Please enter a valid number")  # Handle invalid input

# Create the main window
window = Tk()
window.title("Mile to Kilometer Converter")  # Set the title of the window
window.minsize(width=300, height=150)  # Set the minimum size of the window

# Label for instruction
instruction_label = Label(window, text="Enter distance in miles:", font=("Arial", 14))
instruction_label.grid(column=0, row=0, padx=10, pady=10)  # Place the instruction label in the grid

# Entry widget for miles input
miles_entry = Entry(window, width=15)
miles_entry.grid(column=1, row=0, padx=10, pady=10)  # Place the entry widget in the grid

# Convert button
convert_button = Button(window, text="Convert", command=convert_miles_to_kilometers)
convert_button.grid(column=0, row=1, columnspan=2, pady=10)  # Place the button in the grid spanning two columns

# Result label
result_label = Label(window, text="", font=("Arial", 12))
result_label.grid(column=0, row=2, columnspan=2, pady=10)  # Place the result label in the grid spanning two columns

# Start the Tkinter event loop
window.mainloop()
