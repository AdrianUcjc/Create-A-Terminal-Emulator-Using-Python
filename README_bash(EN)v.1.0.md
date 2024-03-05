# Implement the following program using a BASH Script

The bash will be in charge of executing the following tasks:
The python program called terminal.py is launched from another script and killed from the console!

- The script to launch your program is called launcher.sh
- This launcher has to be able to print the PID of itself (using $$ inside an echo)
- You have to launch the python program called terminal.py from the script
- At the end you will have to be able to close your program from the Linux terminal. For this you need:
    - Know the PID (the ) of the parent process (launcher.sh is supposed to print it)
    - Find the PID of the child with “pstree” and then the PID of the launcher.
        - If pstree does not show you the PIDs
    - Using the son's PID to kill him using “kill -9"

To achieve the functionality, we'll create two scripts: launcher.sh to launch the terminal.py Python program and print its PID, and a mechanism to kill the terminal.py process from the console using the PID of launcher.sh.

### Step 1: Create launcher.sh
This script will launch terminal.py and print its PID. It will also print its own PID.


```
#!/bin/bash

# Launch terminal.py and capture its PID
python3 terminal.py &
TERMINAL_PID=$!

# Print the PID of the launcher script
echo "Launcher script PID: $$"
echo "Terminal script PID: $TERMINAL_PID"

# Wait for the terminal script to complete (optional, for demonstration purposes)
wait $TERMINAL_PID
```


### Step 2: Killing terminal.py from the Console

To kill terminal.py from the console, you need to:

Find the PID of launcher.sh (which you already have from the echo command).
Use pstree or a similar tool to find the PID of terminal.py (child process of launcher.sh).
Kill terminal.py using kill -9.
Using pstree
First, ensure you have pstree installed on your system. If not, you can install it using your package manager (e.g., sudo apt-get install psmisc on Debian/Ubuntu).

You can use pstree to find the PID of terminal.py as follows:

```

pstree -p | grep terminal.py

```

This command lists the process tree and filters for terminal.py. The PID of terminal.py will be part of the output.

Killing the Process
Once you have the PID of terminal.py, you can kill it using:


```
kill -9 <PID>
```

Replace <PID> with the actual PID of terminal.py.

### Note
The launcher.sh script prints the PID of terminal.py immediately after launching it. This is useful for scripting purposes but might not be practical for manual killing from the console.
The wait $TERMINAL_PID command in launcher.sh is optional and is included here for demonstration purposes. It makes the script wait for terminal.py to complete before exiting.
Ensure you have the necessary permissions to execute launcher.sh and terminal.py. You might need to use chmod +x launcher.sh to make launcher.sh executable.
This approach provides a basic mechanism for launching and managing a Python script from a Bash script, including the ability to kill the Python script from the console.
