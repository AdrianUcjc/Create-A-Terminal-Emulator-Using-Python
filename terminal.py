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
