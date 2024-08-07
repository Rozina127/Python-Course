from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Colors used in the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Font settings
FONT_NAME = "Courier"

# Time settings (in minutes)
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Variables to keep track of the number of repetitions and the timer object
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Resets the timer and UI elements to their initial state.
    """
    # Cancel the ongoing timer
    window.after_cancel(timer)
    # Reset the timer display to "00:00"
    canvas.itemconfig(timer_text, text="00:00")
    # Reset the title label to "Timer"
    title_label.config(text="Timer")
    # Clear the check marks label
    check_marks.config(text="")
    # Reset the repetitions counter
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Starts the timer based on the current repetition state.
    """
    global reps
    reps += 1  # Increment the repetitions count

    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine which timer to start
    if reps % 8 == 0:
        count_down(long_break_sec)  # Long break
        title_label.config(text="Break", fg=RED)  # Update title label
    elif reps % 2 == 0:
        count_down(short_break_sec)  # Short break
        title_label.config(text="Break", fg=PINK)  # Update title label
    else:
        count_down(work_sec)  # Work period
        title_label.config(text="Work", fg=GREEN)  # Update title label

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
    Handles the countdown of the timer.
    """
    # Calculate minutes and seconds from the total count
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Format seconds to always display two digits
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Update the timer display on the canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # Continue counting down if the count is greater than zero
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Call count_down again after 1 second
    else:
        start_timer()  # Start the next timer session
        # Update check marks to show completed work sessions
        marks = ""
        work_sessions = math.floor(reps / 2)  # Number of completed work sessions
        for _ in range(work_sessions):
            marks += "✔"  # Add a check mark for each completed work session
        check_marks.config(text=marks)  # Update the check marks label

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # Create the main window
window.title("Pomodoro Timer")  # Set the window title
window.config(padx=100, pady=50, bg=YELLOW)  # Set padding and background color

# Title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)  # Place the title label in the grid at column 1, row 0

# Canvas for timer display
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Load and display the tomato image
try:
    tomato_img = PhotoImage(file="day28_tomato.png")
    canvas.create_image(100, 112, image=tomato_img)  # Place the image in the center of the canvas
except TclError:
    print("Error: Tomato image file not found. Make sure 'tomato.png' is in the correct directory.")
# Create text item for timer display
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)  # Place the canvas in the grid at column 1, row 1

# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer, bg=GREEN, fg=YELLOW, font=(FONT_NAME, 14, "bold"))
start_button.grid(column=0, row=2)  # Place the start button in the grid at column 0, row 2

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, bg=RED, fg=YELLOW, font=(FONT_NAME, 14, "bold"))
reset_button.grid(column=2, row=2)  # Place the reset button in the grid at column 2, row 2

# Check marks label
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)  # Place the check marks label in the grid at column 1, row 3

# Start the Tkinter event loop
window.mainloop()
