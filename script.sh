#!/bin/bash

# Launch terminal.py and capture its PID
python3 terminal.py &
TERMINAL_PID=$!

# Print the PID of the launcher script
echo "Launcher script PID: $$"
echo "Terminal script PID: $TERMINAL_PID"

# Wait for the terminal script to complete (optional, for demonstration purposes)
wait $TERMINAL_PID
