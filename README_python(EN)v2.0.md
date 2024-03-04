# Create-A-Terminal-Emulator-Using-Python

## In this proyect, we will learn how to use tkinter and subproccess, to emulate a unix terminal and replicate most of its functions an applications.

ANSWER | PHIND-34B MODEL

Creating a Unix terminal emulator that opens in a window using Python involves a few steps. You'll need to use a library that can create a graphical window and execute shell commands. For this purpose, we'll use tkinter for the graphical interface and subprocess for executing shell commands.

### Step 1: Install Necessary Libraries
Ensure you have Python installed. tkinter is included in the standard library, so you don't need to install it separately.

### Step 2: Create a Basic Window
First, you'll create a basic window using tkinter. This window will serve as the container for your terminal emulator.

```py
import tkinter as tk

def create_terminal_window():
    window = tk.Tk()
    window.title("Python Terminal Emulator")
    return window

if __name__ == "__main__":
    window = create_terminal_window()
    window.mainloop()
```


### Step 3: Add a Text Widget for Output
Next, add a Text widget to the window. This widget will display the output of the commands executed in the terminal.

```py
import tkinter as tk

def create_terminal_window():
    window = tk.Tk()
    window.title("Python Terminal Emulator")

    output_text = tk.Text(window, wrap=tk.WORD)
    output_text.pack(fill=tk.BOTH, expand=True)

    return window

if __name__ == "__main__":
    window = create_terminal_window()
    window.mainloop()
```

### Step 4: Implement Command Execution
Now, you'll need to implement a way to execute shell commands and display the output in the Text widget. This involves capturing the standard output and standard error of the executed commands.

```py

import tkinter as tk
import subprocess

def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    return stdout.decode('utf-8') + stderr.decode('utf-8')

def on_enter(event, input_entry, output_text):
    command = input_entry.get()
    output_text.insert(tk.END, command + "\n")
    output_text.insert(tk.END, execute_command(command) + "\n")
    input_entry.delete(0, tk.END)

def create_terminal_window():
    window = tk.Tk()
    window.title("Python Terminal Emulator")

    output_text = tk.Text(window, wrap=tk.WORD)
    output_text.pack(fill=tk.BOTH, expand=True)

    input_entry = tk.Entry(window)
    input_entry.bind("<Return>", lambda event: on_enter(event, input_entry, output_text))
    input_entry.pack(side=tk.BOTTOM, fill=tk.X)

    return window

if __name__ == "__main__":
    window = create_terminal_window()
    window.mainloop()
```

### Step 5: Handle Input
The on_enter function is triggered when the user presses Enter in the input field. It captures the command from the input field, executes it, and displays the output in the Text widget.

Final Notes
This is a basic implementation of a terminal emulator in Python using tkinter. It's a starting point that you can expand upon. For example, you could add features like:

Implementing more shell features (e.g., piping, redirection).
Handling more complex input scenarios (e.g., multiple lines of input).
Adding a history of commands.
Improving the user interface and experience.
Remember, running arbitrary shell commands can be dangerous if not handled carefully. Always validate and sanitize inputs to prevent command injection attacks.

### Step 6: Customize te tkinter window
We will be chanching the font colour to green and the background to black for a more aesthetically pleasing terminal.
For this, we will implement the next programm:

For the black background:

```py
window.configure(bg='black')
```
For the green promt text:
```py
output_text = tk.Text(window, wrap=tk.WORD, fg='green', bg='black')
    output_text.tag_configure('input', foreground='green')
    output_text.tag_configure('output', foreground='green')
    output_text.pack(fill=tk.BOTH, expand=True)
```

### Step 7: Make custom commands
Next up, we are going to create 3 custom commands that will have different functionalities.
For this, we will create 3 sub-functions and one main-function.

1st Command:
Use: Output an emoji on the terminal.
```py
def display_emoji(output_text):
    emoji = "😊"
    output_text.insert(tk.END, emoji + "\n")
```

2nd Command:
Use: Open a youtube link.
For this, we will need to import the webbrowser library.

```py
def open_chrome():
    webbrowser.open("https://www.youtube.com/watch?v=mCqVn_GUQz4")
```

3rd Command:
Use: Display a random joke in yellow text.
For this we will need to import the ramdom library, and input a few strings which will contain some jokes.

```py
def display_joke(output_text):
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    ]
    random_joke = random.choice(jokes)
    output_text.insert(tk.END, f"\033[93m{random_joke}\033[0m\n")  # Display in yellow text
```

Main function:
```py
def on_enter(event, input_entry, output_text):
    command = input_entry.get()
    output_text.insert(tk.END, command + "\n")

    if command == "1":
        display_emoji(output_text)
    elif command == "2":
        open_chrome()
    elif command == "3":
        display_joke(output_text)
    
    elif command.lower() == "exit":
        terminate_program(window)

    else:
        output_text.insert(tk.END, execute_command(command) + "\n")

    input_entry.delete(0, tk.END)
```


### Final Code:

```py
import tkinter as tk
import subprocess
import webbrowser
import random

def execute_command(command):
    if command.lower() == "exit":
        window.destroy()  # Terminate the program if "exit" is entered
    else:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8') + stderr.decode('utf-8')

def display_emoji(output_text):
    ascii_art_emoji = """
    ( ͡❛ ͜ʖ ͡❛)
    """
    output_text.insert(tk.END, ascii_art_emoji + "\n")

def open_youtube():
    webbrowser.open("https://www.youtube.com/watch?v=mCqVn_GUQz4")

def display_joke(output_text):
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    ]
    random_joke = random.choice(jokes)
    output_text.insert(tk.END, f"\033[93m{random_joke}\033[0m\n", 'output')  # Display in yellow text

def on_enter(event, input_entry, output_text):
    command = input_entry.get()
    output_text.insert(tk.END, command + "\n", 'input')

    if command == "1":
        display_emoji(output_text)
    elif command == "2":
        open_youtube()
    elif command == "3":
        display_joke(output_text)
    else:
        output_text.insert(tk.END, execute_command(command) + "\n", 'output')

    input_entry.delete(0, tk.END)

def create_terminal_window():
    window = tk.Tk()
    window.title("Python Terminal Emulator")

    # Configuration for black background and green text
    window.configure(bg='black')

    output_text = tk.Text(window, wrap=tk.WORD, fg='green', bg='black')
    output_text.tag_configure('input', foreground='green')
    output_text.tag_configure('output', foreground='green')
    output_text.pack(fill=tk.BOTH, expand=True)

    input_entry = tk.Entry(window, fg='green', bg='black')
    input_entry.bind("<Return>", lambda event: on_enter(event, input_entry, output_text))
    input_entry.pack(side=tk.BOTTOM, fill=tk.X)

    return window

if __name__ == "__main__":
    window = create_terminal_window()
    window.mainloop()
```
